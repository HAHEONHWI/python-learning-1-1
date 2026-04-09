a = input()
alpha = 0
digit = 0
space = 0
other = 0
for i in a:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print(f"영문자: {alpha}")
print(f"숫자: {digit}")
print(f"공백: {space}")
print(f"기타문자: {other}")