
password = input("비밀번호를 입력하세요: ")

count_dict = {
    "영문자": 0,
    "숫자": 0,
    "특수문자": 0
}

for char in password:
    if char.isalpha():
        count_dict["영문자"] += 1
    elif char.isdigit():
        count_dict["숫자"] += 1
    else:
        count_dict["특수문자"] += 1

print(count_dict)