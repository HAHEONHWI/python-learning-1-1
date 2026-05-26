class Subject:
    # 과목별 입력값과 계산된 우선순위를 함께 저장하는 클래스
    def __init__(self, name, days_left, difficulty, importance, study_amount):
        self.name = name
        self.days_left = days_left
        self.difficulty = difficulty
        self.importance = importance
        self.study_amount = study_amount
        self.score = 0
        self.study_level = ""

    def calculate_score(self):
        # 시험이 가까울수록, 난이도/중요도가 높을수록 점수를 높게 계산
        self.score = (
            max(0, 10 - self.days_left) * 3
            + self.difficulty * 3
            + self.importance * 2
            + (10 - self.study_amount) * 2
        )


def positive_number(message):
    # 0보다 큰 정수만 받기 위한 입력 검증
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("0보다 큰 숫자를 입력하세요.")
        except ValueError:
            print("숫자로 입력하세요.")


def range_number(message):
    # 1~10 사이의 값만 받기 위한 입력 검증
    while True:
        try:
            value = int(input(message))
            if 1 <= value <= 10:
                return value
            else:
                print("1부터 10 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자로 입력하세요.")


subjects = []

# 전체 공부 가능 시간과 과목 수를 먼저 입력받는다
total_study_time = positive_number("총 공부 가능 시간을 입력하세요: ")
subject_count = positive_number("과목 수를 입력하세요: ")

for i in range(subject_count):
    # 과목별 정보 입력
    print(f"\n[{i + 1}번째 과목 입력]")

    name = input("과목명: ")
    days_left = positive_number("시험까지 남은 날짜: ")
    difficulty = range_number("난이도(1~10): ")
    importance = range_number("중요도(1~10): ")
    study_amount = range_number("지금까지 공부한 양(1~10): ")

    subject = Subject(name, days_left, difficulty, importance, study_amount)
    subjects.append(subject)

# 각 과목의 우선순위 점수 계산
for subject in subjects:
    subject.calculate_score()

# 점수가 높은 과목부터 정렬
subjects.sort(key=lambda subject: subject.score, reverse=True)

count = len(subjects)

# 정렬 결과를 기준으로 공부 비중을 3단계로 나눈다
for i, subject in enumerate(subjects):
    if i < count / 3:
        subject.study_level = "비교적 많이"
    elif i < count * 2 / 3:
        subject.study_level = "중간"
    else:
        subject.study_level = "비교적 적게"

print("\n===== 시험공부 계획 =====")
print(f"총 공부 가능 시간: {total_study_time}시간")
print("========================")

    # 최종 우선순위와 추천 공부량 출력
for i, subject in enumerate(subjects, start=1):
    print(f"{i}순위: {subject.name}")
    print(f"시험까지 남은 날짜: {subject.days_left}일")
    print(f"우선순위 점수: {subject.score}")
    print(f"추천 공부 시간: {subject.study_level}")
    print("------------------------")