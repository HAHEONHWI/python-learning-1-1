class Subject:
    def __init__(self, name, days_left, difficulty, importance, study_amount):
        self.name = name
        self.days_left = days_left
        self.difficulty = difficulty
        self.importance = importance
        self.study_amount = study_amount
        self.score = 0
        self.study_level = ""