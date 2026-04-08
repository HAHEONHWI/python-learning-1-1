students = [
    [101, "김민준", "로봇"],
    [102, "이서연", "방송"],
    [103, "박지후", "로봇"],
    [104, "최하은", "도서"]
]

students_dict = {}

target_id = 103

for a, b, c in students:
    students_dict[a] = [b, c]

print(students_dict)

print(students_dict[target_id][0], students_dict[target_id][1])


club_count = {}

for i in students:
    club = i[2]

    if club in club_count:
        club_count[club] += 1
    else:
        club_count[club] = 1 

print(club_count)