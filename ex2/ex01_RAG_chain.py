import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from openaikey import openai_key
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
from langchain import hub
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = openai_key
llm = ChatOpenAI(model="gpt-4o-mini")


def get_docs() :
    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]


    loader_multiple_pages = WebBaseLoader(urls)
    loader_multiple_pages.requests_per_second = 1
    return loader_multiple_pages.aload()

def split(text) :
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=500,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.create_documents([text])
    return texts

def get_retriever(documents):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        # With the `text-embedding-3` class
        # of models, you can specify the size
        # of the embeddings you want returned.
        # dimensions=1024
    )

    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not neccesary
    )

    uuids = [str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=uuids)

    return vector_store.as_retriever(
        search_type="mmr", search_kwargs={'k': 6}
    )

def chunks_to_evaluate_prompt(chunks):
    prompt = hub.pull("rlm/rag-prompt")
    prompt_messages = []
    for chunk in chunks:
        temp_message = prompt.invoke({"context": f"""
            retriever_chunk => {chunk.page_content}
            user_query => {{user_query}}
            """, "question": """
            retriever_chunk 와 user_query 간 유사도 점수를 매겨라. 최소 점수는 0점 최대 점수는 100점이다.
            답변은 json string 형태로 하라. score(점수), chunk(context로 전달된 retriever_chunk) 를 키로 갖는 json string 형태로 반환하라.
            """}).to_messages()
        print("=======================================================================")
        print(chunk.page_content)
        print("=======================================================================")
        print(temp_message)

        prompt_messages += temp_message
    return prompt_messages





docs = get_docs()
splitted_docs = []
for doc in docs:
    splitted_docs += split(doc.page_content)

retriever = get_retriever(splitted_docs)
real_query = "What is prompt engineering?"
# fake_query = "pig"
user_query = real_query

retriever_chunks = retriever.invoke(user_query)
prompt_messages = chunks_to_evaluate_prompt(retriever_chunks)

for prompt_message in prompt_messages:
    parser = JsonOutputParser()
    prompt = PromptTemplate(
        template=prompt_message.content,
        input_variables=["user_query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser
    chain.invoke({"user_query": user_query})