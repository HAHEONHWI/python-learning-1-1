class Subject:
    def __init__(self, name, days_left, difficulty, importance, study_amount):
        self.name = name
        self.days_left = days_left
        self.difficulty = difficulty
        self.importance = importance
        self.study_amount = study_amount
        self.score = 0
        self.study_level = ""

    def calculate_score(self):
        self.score = (
            max(0, 10 - self.days_left) * 3
            + self.difficulty * 3
            + self.importance * 2
            + (10 - self.study_amount) * 2
        )


def input_positive_number(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            else:
                print("0보다 큰 숫자를 입력하세요.")
        except ValueError:
            print("숫자로 입력하세요.")


def input_range_number(message):
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

total_study_time = input_positive_number("총 공부 가능 시간을 입력하세요: ")
subject_count = input_positive_number("과목 수를 입력하세요: ")

for i in range(subject_count):
    print(f"\n[{i + 1}번째 과목 입력]")

    name = input("과목명: ")
    days_left = input_positive_number("시험까지 남은 날짜: ")
    difficulty = input_range_number("난이도(1~10): ")
    importance = input_range_number("중요도(1~10): ")
    study_amount = input_range_number("지금까지 공부한 양(1~10): ")

    subject = Subject(name, days_left, difficulty, importance, study_amount)
    subjects.append(subject)

for subject in subjects:
    subject.calculate_score()

subjects.sort(key=lambda subject: subject.score, reverse=True)

count = len(subjects)

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

for i, subject in enumerate(subjects, start=1):
    print(f"{i}순위: {subject.name}")
    print(f"시험까지 남은 날짜: {subject.days_left}일")
    print(f"우선순위 점수: {subject.score}")
    print(f"추천 공부 시간: {subject.study_level}")
    print("------------------------")