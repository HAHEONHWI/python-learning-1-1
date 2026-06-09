from recommend import recommend_food, find_same_score
from gemini_api import get_reason, choose_same_score_food


def input_choice(text, choices):
    while True:
        print()
        print(text)
        print("선택 가능:", ", ".join(choices))

        value = input("입력: ").strip()

        if value in choices:
            return value

        print("잘못 입력했습니다. 다시 입력해주세요.")


def input_number(text, start, end):
    while True:
        try:
            value = int(input(text))

            if start <= value <= end:
                return value

            print(start, "부터", end, "사이의 숫자를 입력해주세요.")

        except ValueError:
            print("숫자만 입력해주세요.")


def input_soup():
    while True:
        print()
        print("국물 있는 메뉴를 원하나요?")
        print("선택 가능: ㅇㅇ, ㄴㄴ, 아무거나")

        value = input("입력: ").strip()

        if value == "ㅇㅇ":
            return True
        elif value == "ㄴㄴ":
            return False
        elif value == "아무거나":
            return None
        else:
            print("잘못 입력했습니다. 다시 입력해주세요.")


def get_user():
    user = {}

    user["country"] = input_choice(
        "선호 음식 종류를 선택하세요.",
        ["한식", "중식", "양식", "일식", "아무거나"]
    )

    user["food_type"] = input_choice(
        "먹고 싶은 음식 형태를 선택하세요.",
        ["쌀/밥", "면", "떡", "전", "육류", "빵", "기타", "아무거나"]
    )

    user["spicy"] = input_number(
        "\n매운맛 허용 정도를 입력하세요. 0은 안 매운 것, 5는 매운 것 선호: ",
        0,
        5
    )

    user["soup"] = input_soup()

    user["mood"] = input_choice(
        "오늘 원하는 느낌을 선택하세요.",
        ["든든하게", "가볍게", "따뜻하게", "아무거나"]
    )

    return user


def print_foods(foods):
    print()
    print("========== 추천 결과 ==========")

    if len(foods) == 0:
        print("조건에 맞는 메뉴가 없습니다.")
        print("조건을 조금 바꿔서 다시 입력해보세요.")
        return

    rank = 1

    for food in foods:
        if food["spicy"] == True:
            spicy_text = "매움"
        elif food["spicy"] == False:
            spicy_text = "안 매움"
        else:
            spicy_text = "매운맛 정보 없음"

        if food["soup"] == True:
            soup_text = "국물 있음"
        elif food["soup"] == False:
            soup_text = "국물 없음"
        else:
            soup_text = "국물 정보 없음"

        print()
        print(str(rank) + "위:", food["name"])
        print("분류:", food["country"], "/", food["type"])
        print("특징:", spicy_text + ",", soup_text)
        print("추천 점수:", str(food["score"]) + "점")

        if len(food["reason"]) > 0:
            print("추천 이유:", ", ".join(food["reason"]))

        rank += 1


def main():
    print("================================")
    print("오늘 뭐먹지")
    print("사용자 맞춤 메뉴 추천 프로그램")
    print("================================")

    while True:
        user = get_user()

        top_foods = recommend_food(user)

        print_foods(top_foods)

        if len(top_foods) > 0:
            same_foods = find_same_score(top_foods)

            if len(same_foods) >= 2:
                print()
                print("========== Gemini AI 동점 최종 추천 ==========")
                tie_answer = choose_same_score_food(same_foods, user)
                print(tie_answer)

            print()
            print("========== Gemini AI 추천 사유 ==========")
            ai_answer = get_reason(top_foods, user)
            print(ai_answer)

        print()
        again = input("다시 추천받을까요? (ㅇㅇ / ㄴㄴ): ").strip()

        if again != "ㅇㅇ":
            print("프로그램을 종료합니다.")
            break


main()