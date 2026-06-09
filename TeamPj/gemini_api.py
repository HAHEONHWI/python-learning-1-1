import os
import time
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


def ask_gemini(prompt):
    if not api_key:
        return "Gemini API 키가 없습니다. .env 파일을 확인해주세요."

    client = genai.Client(api_key=api_key)

    for retry in range(3):
        try:
            answer = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            if answer.text:
                return answer.text
            else:
                return "Gemini가 빈 응답을 반환했습니다."

        except Exception as e:
            error_text = str(e)

            if "503" in error_text or "UNAVAILABLE" in error_text:
                if retry < 2:
                    time.sleep(retry + 1)
                    continue

                return "Gemini 서버가 지금 바빠서 AI 추천을 가져오지 못했습니다. 잠시 후 다시 실행해주세요."

            return "Gemini API 오류: " + error_text


def get_reason(top_foods, user):
    prompt = f"""
너는 메뉴 추천 프로그램의 설명 담당 AI야.

사용자가 입력한 조건:
{user}

우리 프로그램이 계산한 추천 결과:
{top_foods}

위 내용을 보고 추천 이유를 3문장 정도로 설명해줘.

조건:
1. 추천 결과에 없는 메뉴를 새로 만들지 마.
2. 1위 메뉴가 왜 적합한지 중심으로 설명해.
3. 고등학생이 이해하기 쉽게 말해.
"""

    return ask_gemini(prompt)


def choose_same_score_food(same_foods, user):
    names = []

    for food in same_foods:
        names.append(food["name"])

    prompt = f"""
너는 메뉴 추천 프로그램에서 동점 메뉴를 골라주는 AI야.

사용자 조건:
{user}

동점 메뉴 목록:
{names}

위 동점 메뉴 중에서 사용자 조건에 가장 잘 맞는 메뉴 하나만 골라줘.

출력 형식은 꼭 아래처럼 해줘.

최종 추천: 메뉴이름
이유: 설명

조건:
1. 동점 메뉴 목록 안에서만 골라.
2. 새로운 메뉴를 만들지 마.
3. 이유는 2문장 정도로 짧게 써.
"""

    return ask_gemini(prompt)
