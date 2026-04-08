import os

a = int(input("a: "))
b = int(input("b: "))

folder_path = "/Users/dgsw09/수업/py/0406"

# 폴더 없으면 생성
os.makedirs(folder_path, exist_ok=True)

for i in range(a, b + 1):
    file_path = os.path.join(folder_path, f"{i}.py")

    with open(file_path, "w", encoding="utf-8") as f:
        pass

    print(f"{i}.py 생성됨")