data = [
  ("김민준", "국어", 80),
  ("김민준", "영어", 90),
  ("이서연", "국어", 100),
  ("이서연", "영어", 95)
]
student_scores = {}
subject_scores = {}   
for name, subject, score in data:
    if name not in student_scores:
        student_scores[name] = {}
    student_scores[name][subject] = score
    if subject not in subject_scores:
        subject_scores[subject] = []
    subject_scores[subject].append(score)

averages = {}

for name, scores in student_scores.items(): 
    average = sum(scores.values()) / len(scores) 
    averages[name] = average

print(student_scores)

for name, avg in averages.items():
    print(name, avg)

for subject, scores in subject_scores.items():
    average = sum(scores) / len(scores)
    print(subject, average)