from openai import OpenAI
from openaikey import openai_key
import os
import pprint


os.environ["OPENAI_API_KEY"] = openai_key
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "특별한 순서로 계산해보자"
        },
        {
            "role": "system",
            "content": "step 1. 각각 항의 자릿수별로 분리한다. 예를 들자면 123 + 53 은 100 + 20 + 3 + 50 + 3 으로 분리하자"
        },
        {
            "role": "system",
            "content": "step 2. 같은 자리수 끼리 먼저 더하자. 위의 예시에서 스텝 2를 진행하면 100 + 70 + 6 이 된다."
        },
        {
            "role": "system",
            "content": "step 3. 이제 모든 자릿수의 연산 결과를 연산하자. 위의 예시에서 스텝 3을 진행하면 176 이 된다."
        },
        {
            "role": "user",
            "content": "내가 알려준 순서대로 다음을 풀어봐: 23 + 47. 그리고 스텝별 풀이과정을 출력해줘"
        }
    ]
)

print(completion.choices[0].message.content)


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "특별한 순서로 계산해보자"
        },
        {
            "role": "system",
            "content": "step 1. 각각 항의 자릿수별로 분리한다. 예를 들자면 123 + 53 은 100 + 20 + 3 + 50 + 3 으로 분리하자"
        },
        {
            "role": "system",
            "content": "step 2. 같은 자리수 끼리 먼저 계산하자. 위의 예시에서 스텝 2를 진행하면 100 + 70 + 6 이 된다."
        },
        {
            "role": "system",
            "content": "step 3. 이제 모든 자릿수의 연산 결과를 연산하자. 위의 예시에서 스텝 3을 진행하면 176 이 된다."
        },
        {
            "role": "user",
            "content": "내가 알려준 순서대로 다음을 풀어봐: 123-58. 그리고 스텝별 풀이과정을 출력해줘"
        }
    ]
)

print(completion.choices[0].message.content)




completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "특별한 순서로 계산해보자"
        },
        {
            "role": "system",
            "content": "step 1. 각각 항의 자릿수별로 분리한다. 예를 들자면 123 + 53 은 100 + 20 + 3 + 50 + 3 으로 분리하자"
        },
        {
            "role": "system",
            "content": "step 2. 같은 자리수 끼리 먼저 계산하자. 위의 예시에서 스텝 2를 진행하면 100 + 70 + 6 이 된다."
        },
        {
            "role": "system",
            "content": "step 3. 이제 모든 자릿수의 연산 결과를 연산하자. 위의 예시에서 스텝 3을 진행하면 176 이 된다."
        },
        {
            "role": "user",
            "content": "내가 알려준 순서대로 다음을 풀어봐: 345 + 678 - 123. 그리고 스텝별 풀이과정을 출력해줘"
        }
    ]
)

print(completion.choices[0].message.content)











completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Solve the following logic puzzle step-by-step:"
                       "Three friends, Alice, Bob, and Carol, have different favorite colors: red, blue, and green. We know that:"
                       "1. Alice does not like red."
                       "2. Bob does not like blue."
                       "3. Carol likes green."
        },
        {
            "role": "user",
            "content": "Determine the favorite color of each friend"
        }
    ]
)

print(completion.choices[0].message.content)





completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Solve the following logic puzzle step-by-step:"
                       "Four people (A, B, C, D) are sitting in a row. We know that:"
                       "1. A is not next to B."
                       "2. B is next to C."
                       "3. C is not next to D."
        },
        {
            "role": "user",
            "content": "Determine the possible seating arrangements."
        }
    ]
)

print(completion.choices[0].message.content)