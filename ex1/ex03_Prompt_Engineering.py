from openai import OpenAI
from openaikey import openai_key
import os

os.environ["OPENAI_API_KEY"] = openai_key
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "영어를 한글로 번역해줘."
        },
        {
            "role": "system",
            "content": "Apple => 사과, Banana => 바나나, House => 집, Man => 남자, Sky => 하늘."
        },
        {
            "role": "user",
            "content": "Dog 를 한글로 번역해줘"
        }
    ]
)

print(completion.choices[0].message)







completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "영화 리뷰를 해보자"
        },
        {
            "role": "system",
            "content": "영화 1 리뷰 => 재미있다."
        },
        {
            "role": "system",
            "content": "영화 2 리뷰 => 혼란스럽다."
        },
        {
            "role": "system",
            "content": "영화 3 리뷰 => 웃기다."
        },
        {
            "role": "system",
            "content": "영화 4 리뷰 => 무섭다."
        },
        {
            "role": "system",
            "content": "영화 5 리뷰 => 지루하다."
        },
        {
            "role": "user",
            "content": "The storyline was dull and uninspiring 인 영화는 어떤것인가?"
        }
    ]
)

print(completion.choices[0].message)













completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "자연어 문장을 SQL로 번역해보자 !!"
        },
        {
            "role": "system",
            "content": "1. 급여가 5만원이 넘는 직원 조회: SELECT * FROM employees WHERE salary > 50000;"
        },
        {
            "role": "system",
            "content": "2. 수량이 0인 제품을 조회: SELECT * FROM products WHERE stock = 0;"
        },
        {
            "role": "system",
            "content": "3. 수학점수가 90점이 넘는 학생의 이름을 조회: SELECT name FROM students WHERE math_score > 90;"
        },
        {
            "role": "system",
            "content": "4. 최근 30일간 주문건 조회: SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);"
        },
        {
            "role": "system",
            "content": "5. 도시별 고객 수 조회: SELECT city, COUNT(*) FROM customers GROUP BY city;"
        },
        {
            "role": "user",
            "content": "Find the average salary of employees in the marketing department."
        }
    ]
)







print(completion.choices[0].message)