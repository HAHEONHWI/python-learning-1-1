print('실제 주민번호 판별식을 이용하여 구하는 주민번호 판별하기')

a, b, c, d, e, f = map(int, list(input('주민번호 앞자리')))
g, h, i, j, k, l, x = map(int, list(input('주민번호 뒷자리')))
n = (2*a + 3*b + 4*c + 5*d + 6*e + 7*f +
     8*g + 9*h + 2*i + 3*j + 4*k + 5*l)
def number(country):
    return (country - (n % 11)) % 10

print(n)

if 10*a+b > 28 and g == (1 or 2 or 5 or 6): #19세기사람
    pass
    if g == 1 or 2:
        if number(int(11)) == x:
            if g == 1:
                print('1900년대 남자 내국인 주민번호 성립')
            else:
                print('1900년대 여자 내국인 주민번호 성립')
        else:
            print('잘못된 주민번호')
    elif g == 5 or 6:
        if number(int(13)) == x:
            if g == 5:
                print('1900년대 남자 외국인 주민번호 성립')
            else:
                print('1990년대 여자 주민번호 성립')

        else:
            print('잘못된 주민번호')

elif 10*a+b < 28 and g == (3 or 4 or 7 or 8): #20세기사람
    pass
    if g == 3 or 4 and 10*a+b >20:
        if number(int(11)) == x:
            if g == 3:
                print('2000년대 내국인 남자 주민번호 성립')
            else:
                print('2000년대 내국인 여자 주민번호 성립')
        else:
            print('잘못된 주민번호')
    if g == 7 or 8 and 10*a+b >20:
        if number(int(13)) == x:
            if g == 7:
                print('2000년대 남자 외국인 주민번호 성립')
            else:
                print('2000년대 여자 외국인 주민번호 성립')
        else:
            print('잘못된 주민번호')
else:
    print('잘못된 주민번호(생일 이상)')
    