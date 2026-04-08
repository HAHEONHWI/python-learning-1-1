import random as r , time
word = ['hello',  'apple', 'samsung', 'cat', 'monkey', 'mouse', 'panda', 'frog', 'snake']
point = 0
num = 1
start = time.time()

if input('준비되면 엔터') == '':
    while True :
        if point < 5:
            print(f'\n[문제 {num}]')
            w = r.choice(word)
            print(w)
            if input() == w :
                print('\npass')
                point += 1
                num += 1
            else:
                print('\nFail')
                num += 0
                w = r.choice(word)
                pass
        else:
            break
    end = time.time()
    print('걸린 시간 :', end-start)