'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~10) 다섯 개를 추가한 후,  5보다 큰수만 출력하시오.
        [조건2] 위 조건의 개수를 출력하시오.
'''
import random
arr = []

for i in range(5) :
    randomNumber = random.randint(1, 10)
    arr.append(randomNumber)
print("arr = ", arr)

cnt = 0
for i in range(len(arr)) :
    bigFive = arr[i] > 5
    if bigFive :
        cnt+= 1
print(f"5보다 큰 수는 총 {cnt}개 ")