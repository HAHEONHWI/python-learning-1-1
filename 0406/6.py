courses = {
    "김민준": ["파이썬","자료구조"],
    "이서연": ["파이썬","인공지능"],
    "박지후": ["자료구조","인공지능"],
    "최하은": ["파이썬","자료구조"]
}

target = "김민준" #기준 학생 정함
target_courses = set(courses[target]) #set 쓰는 이유:겹치는 과목 찾기 쉬우려고(courses리스트를 집합 set으로 변환) ,집합은 중복을 제거하고 교집합 계산이 쉽다
#특정 대상이 듣는 과목들을 집합 형태로 변환해서 저장
#특정 사람의 과목 리스트를 집합으로 바꿔서 중복 제거+비교를 쉽게 하려고 하는 코드

similar_students = [] #비슷한 과목을 듣는 학생들
recommend = set() #추천 과목

for student, subjects in courses.items(): #모든 학생 검사:한명씩 확인
    if student == target: #김민준은 비교 안함
        continue #계속하기
    
    subjects_set = set(subjects) #특정 학생의 과목도 set으로 바꿈
    
    # 1. 겹치는 과목이 하나라도 있으면
    if target_courses & subjects_set: #겹치는 과목 있는지 확인(&=공통 과목)
        similar_students.append(student) #비슷한 학생 저장
        
        # 2. 추천 과목 추가 (없는 과목만)
        recommend |= (subjects_set - target_courses) #다른 학생들은 듣지만 특정 학생은 안 듣는 과목(|=는 추천 목록에 추가)

print(similar_students)
print(list(recommend))