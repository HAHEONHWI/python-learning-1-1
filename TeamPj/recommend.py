import json
import os


def load_foods():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "foodList_menus.json")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            foods = json.load(file)
        return foods

    except FileNotFoundError:
        print("foodList_menus.json 파일을 찾을 수 없습니다.")
        return []

    except json.JSONDecodeError:
        print("JSON 파일 형식이 잘못되었습니다.")
        return []


def check_food(food, user):
    if food.get("alcohol") == True:
        return False

    if user["country"] != "아무거나":
        if food.get("country") != user["country"]:
            return False

    if user["food_type"] != "아무거나":
        if food.get("type") != user["food_type"]:
            return False

    spicy = food.get("spicy")

    if spicy != None:
        if user["spicy"] == 0 and spicy == True:
            return False

        if user["spicy"] == 5 and spicy == False:
            return False

    soup = food.get("soup")

    if user["soup"] != None and soup != None:
        if user["soup"] != soup:
            return False

    return True


def food_score(food, user):
    score = 10
    reason = []

    if user["country"] == "아무거나":
        score += 5
        reason.append("음식 종류 제한 없음")
    else:
        if food.get("country") == user["country"]:
            score += 30
            reason.append("선호 음식 종류와 일치")

    if user["food_type"] == "아무거나":
        score += 5
        reason.append("음식 형태 제한 없음")
    else:
        if food.get("type") == user["food_type"]:
            score += 25
            reason.append("원하는 음식 형태와 일치")

    spicy = food.get("spicy")

    if spicy == True:
        if user["spicy"] >= 3:
            score += 20
            reason.append("매운맛 선호와 적합")
        else:
            score += 5
            reason.append("조금 매울 수 있음")

    elif spicy == False:
        if user["spicy"] <= 2:
            score += 20
            reason.append("맵지 않은 음식 선호와 적합")
        else:
            score += 10
            reason.append("무난하게 먹기 좋음")

    else:
        score += 5
        reason.append("매운맛 정보 없음")

    soup = food.get("soup")

    if user["soup"] == None:
        score += 5
        reason.append("국물 여부 제한 없음")
    else:
        if soup != None and soup == user["soup"]:
            score += 15

            if soup == True:
                reason.append("국물 있는 메뉴 선호와 일치")
            else:
                reason.append("국물 없는 메뉴 선호와 일치")

    mood = user["mood"]

    if mood == "든든하게":
        if food.get("type") == "쌀/밥" or food.get("type") == "육류":
            score += 10
            reason.append("든든한 식사에 적합")

    elif mood == "가볍게":
        if food.get("type") == "면" or food.get("type") == "빵" or food.get("type") == "기타":
            score += 10
            reason.append("가볍게 먹기 좋은 메뉴")

    elif mood == "따뜻하게":
        if food.get("soup") == True:
            score += 10
            reason.append("따뜻하게 먹기 좋은 메뉴")

    elif mood == "아무거나":
        score += 5
        reason.append("기분 조건 제한 없음")

    return score, reason


def get_score(food):
    return food["score"]


def recommend_food(user, count=3):
    foods = load_foods()
    result = []

    for food in foods:
        if check_food(food, user):
            score, reason = food_score(food, user)

            data = {
                "name": food.get("name"),
                "country": food.get("country"),
                "type": food.get("type"),
                "spicy": food.get("spicy"),
                "soup": food.get("soup"),
                "score": score,
                "reason": reason
            }

            result.append(data)

    result.sort(key=get_score, reverse=True)

    return result[:count]


def find_same_score(top_foods):
    if len(top_foods) == 0:
        return []

    first_score = top_foods[0]["score"]
    same = []

    for food in top_foods:
        if food["score"] == first_score:
            same.append(food)

    return same