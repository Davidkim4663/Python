'''
    [문제]
        [조건1] 리스트에 랜덤 숫자(1~100) 5개를 추가한다.
        [조건2] 위 값 중에 50보다 큰 값들만 출력한다.
    [예시]
        arr = [84, 28, 5, 100, 80]
        84
        100
        80
'''
import random
arr = []
for i in range(5) :
    randomNum = random.randint(1, 100)
    arr.append(randomNum)
print("arr = ",arr)
print()

for i in range(len(arr)) :
    comparsionBig_50 = arr[i] >= 50
    if comparsionBig_50 :
        print(arr[i],end=" ")