'''
    [문제]
        랜덤 숫자(1~10) 다섯 개를 arr에 추가하고
        그 두 배를 total에 저장 후 출력하시오.
    [예시]
        arr   = [10, 3, 4, 2, 6]
        total = [20, 6, 8, 4, 12]
'''
import random

arr = []
total = []

for i in range(5) :
    randNum = random.randint(1, 10)
    arr.append(randNum)
print("arr = ", arr)

for i in range(len(arr)) :
    doubleRand = arr[i] * 2
    total.append(doubleRand)
print("total = ", total)
