def is_palindrome(text):
    text = text.replace(" ", "").lower()

    # 재귀 함수
    def check(left, right):
        if left >= right:
            return True

        if text[left] != text[right]:
            return False

        return check(left + 1, right - 1)

    return check(0, len(text) - 1)


word = input("문자열 입력: ")

if is_palindrome(word):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")