def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            break
        return -1
    
data = [10, 20, 30, 40, 50]
target_value = 25
result = sequential_search(data, target_value)

if result != -1:
    print(f"인덱스 {result}에서 값을 찾았습니다.")
else:
    print('값이 리스트에 존재하지 않습니다')