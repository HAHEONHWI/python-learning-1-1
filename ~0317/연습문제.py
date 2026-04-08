#1번 - 세 개의 변수를 이용한 덧셈 연산
print('1번 - 세 개의 변수를 이용한 덧셈 연산')
a = 50
b = 20
c = a+b
print (a, b, c)
print ('a=', a, 'b=', b, 'c=', c)

#2번 - 이름 입력받아 출력하기
print('\n2번 - 이름 입력받아 출력하기')
name = '친구들'
print(name, "반가워요")

#3번 - 두 수를 입력받아 계산하기
print('\n3번 - 두 수를 입력받아 계산하기\n')
x = int(input('첫 번째 수:'))
y = int(input('두 번째 수:'))
z = x+y
print ("두 수의 합은 ", z)

#4번 - 
print ("\n4번 - ")
print("안녕하세요")
name2 = input("이름이 뭐에요?")
print (name2 + "님 반가워요")
age = int(input('몇살이에요?'))
print('10년 뒤에는', (age + 10), "살이 되는군요!")
food = input('좋아하는 음식은 뭐에요?')
print ("저도", food, '엄청 좋아해요')

#5번 빵값 계산하기, 10% 할인
print('\n#5번 빵값 계산하기, 10% 할인')
price = 800
count = 10
total = price*count
total *= 0.9
print('전체 빵값 :', total)

#6번 빵값 입력받아 계산하기
print('\n#6번 빵값 입력받아 계산하기, 10% 할인')
price = int(input('빵의 단가 입력'))
count = int(input('빵의 개수 입력'))
total = price*count
total *= 0.9
print('전체 빵값 : ',  total)

#7번 BMI 구하는 프로그램
print('\n#7번 BMI 구하는 프로그램')
height = int(input('키 입력'))
weight = int(input('몸무게 입력'))
bmi = weight/(height**2)*10000
print('체질량 지수 : ', bmi)

#8번 파이썬 문방구의 오늘 총 판매 금액 구하기
print('\n#8번 파이썬 문방구의 오늘 총 판매 금액 구하기')
pencil = int(input('연필의 판매개수는?'))
a1 = pencil*700
era = int(input('지우개의 판매 개수는?'))
a2 = era*500
note = int(input('공책의 판매 개수는?'))
a3 = note*2500
print('''
---------------------------------
      파이썬 문방구의 오늘 판매내역 
---------------------------------
''')
print('연필 : ', pencil,  '개, ', a1, '원')
print('지우개 : ', era,  '개, ', a2, '원')
print('공책 : ', note,  '개, ', a3, '원')
print('''---------------------------------''')
print('오늘의 판매 금액', (a1+a2+a3), '원')
print('''---------------------------------''')