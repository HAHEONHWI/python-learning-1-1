def list_avg(s_list):
    sum = 0
    for i in s_list :
        sum = sum + i
    result = sum/len(s_list)
    print('점수의 평균:', result)

score = [90, 80, 70, 60, 50]
list_avg(score)