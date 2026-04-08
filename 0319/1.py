import random as r

user = 100
monster = 120

def all(u_damn, m_damn):
    global user, monster

    user -= m_damn
    monster -= u_damn
    print('나의 체력 :', user)
    print('몬스터의 체력 :', monster)
    print('------------------')

def heal():
    global user
    heal_amount = r.randint(5, 15)
    m_damn = r.randint(1, 5)

    user += heal_amount

    print('회복 된 양 :', heal_amount)
    print('몬스터가 준 데미지 :', m_damn)

    return 0, m_damn

def attack1():
    u_damn = r.randint(2, 10)

    if u_damn > 7:
        print('몬스터가 간지럼을 참지 못했다!')
        print('내가 준 데미지 :', u_damn)
        print('몬스터는 데미지를 주지 못했다')
        return u_damn, 0
    else:
        print('포인트를 잘못잡아 간지럼을 타지 않는다')
        print('내가 준 데미지 :', u_damn)
        m_damn = r.randint(3, 7)
        print('몬스터가 준 데미지 :', m_damn)
        return u_damn, m_damn

def attack2():
    u_damn = r.randint(5, 15)
    m_damn = r.randint(1, 25)

    print('내가 준 데미지 :', u_damn)
    print('몬스터가 준 데미지 :', m_damn)

    return u_damn, m_damn

def attack3():
    u_damn = r.randint(10, 45)
    m_damn = r.randint(20, 30)

    print('내가 준 데미지 :', u_damn)
    print('몬스터가 준 데미지 :', m_damn)

    return u_damn, m_damn
print('''
몬스터를 이겨라
원하는 공격 번호 작성하기
1 : 간지럽히기
2 : 찌르기
3 : 비장의 무기(위험)
4 : 치유하기''')

while user > 0 and monster > 0:
    attack = int(input('공격 번호 선택 (1~4): '))

    if attack == 1:
        u, m = attack1()
    elif attack == 2:
        u, m = attack2()
    elif attack == 3:
        u, m = attack3()
    elif attack == 4:
        u, m = heal()
    else:
        print('잘못된 입력')
        continue

    all(u, m)

if user <= 0:
    print('패배...')
else:
    print('승리!')