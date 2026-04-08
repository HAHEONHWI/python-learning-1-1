height = int(input('키'))
parents = bool(input('보호자 동반 여부'))
age = int(input('나이'))
staff = bool(input('직원 여부'))
safety = bool(input('안전교육여부'))

if staff == True and safety == True:
    print('탑승가능')
elif age >= 65:
    print('탑승불가')
elif 120 <= height <= 140 and parents == True:
    print('보호자 동반시 가능')
elif height >= 140:
    print('탑승가능')
else:
    print("탑승불가")