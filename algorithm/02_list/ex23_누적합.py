'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~10) 5개를 추가하고,
        [조건2] 위 조건의 누적합을 출력하시오.
'''
import random
arr = []
sum = 0
for i in range(5) :
    randomNumber = random.randint(1, 10)
    arr.append(randomNumber)
print("arr = ", arr)

for i in range(len(arr)) :
    sum += arr[i]
print("sum = ", sum)
