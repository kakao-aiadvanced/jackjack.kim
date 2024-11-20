from typing_extensions import TypedDict
from pprint import pprint
from typing import List
from langgraph.graph import END, StateGraph
from ex3.tools import get_retriever, get_retriever_grader, get_answer_generator, get_hallucination_grader

RE_RELEVANCE_CHECK_COUNT = 0
RE_HALLUCINATION_CHECK_COUNT = 0

class GraphState(TypedDict):
    question: str
    generation: str
    web_search: str
    relevance_result: str
    hallucination_result: str
    documents: List[str]

def docs_retrieval(state):
    print("================================= docs_retrieval")
    question = state["question"]
    documents = get_retriever().invoke(question)
    return {"documents": documents, "question": question}

def relevance_checker(state):
    print("================================= relevance_checker")
    result = get_retriever_grader().invoke({"question": state['question'], "document": state['documents']})
    return {"relevance_result": result['score']}

def generate_answer(state):
    print("================================= generate_answer")
    generation = get_answer_generator().invoke({"context": state['documents'], "question": state['question']})
    return {"generation": generation}


def search_tavily(state):
    print("================================= search_tavily")

def hallucination_checker(state):
    print("================================= hallucination_checker")
    result = get_hallucination_grader().invoke({"documents": state['documents'], "generation": state['generation']})
    return {"hallucination_result": result['score']}

def decide_relevance_check(state):
    print("================================= decide_relevance_check")
    if state['relevance_result'] == 'yes' :
        return 'generate_answer'
    else :
        if RE_RELEVANCE_CHECK_COUNT > 0 :
            return 'fail'
        else :
            return 'search_tavily'

def decide_hallucination_check(state):
    print("================================= decide_hallucination_check")
    if state['hallucination_result'] == 'yes' :
        return 'answer_to_user'
    else :
        if RE_HALLUCINATION_CHECK_COUNT > 0 :
            return 'fail'
        else :
            return 'generate_answer'

workflow = StateGraph(GraphState)
workflow.add_node("docs_retrieval", docs_retrieval)
workflow.add_node("relevance_checker", relevance_checker)
workflow.add_node("generate_answer", generate_answer)
workflow.add_node("search_tavily", search_tavily)
workflow.add_node("hallucination_checker", hallucination_checker)

workflow.set_entry_point("docs_retrieval")
workflow.add_edge("docs_retrieval", "relevance_checker")
workflow.add_conditional_edges(
    "relevance_checker",
    decide_relevance_check,
    {
        "generate_answer": "generate_answer",
        "search_tavily": "search_tavily",
        "fail": END
    },
)
workflow.add_edge("generate_answer", "hallucination_checker")
workflow.add_conditional_edges(
    "hallucination_checker",
    decide_hallucination_check,
    {
        "generate_answer": "generate_answer",
        "answer_to_user": END,
        "fail": END
    },
)


app = workflow.compile()
inputs = {"question": "What is prompt?"}
for output in app.stream(inputs):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")
        pprint(value)