'''
    [문제]
        랜덤 숫자 100~200을 다섯 개 저장하고,
        다섯 개 숫자 중에 3의 배수들을 출력하시오.
        3의 배수들의 개수와
        3의 배수들의 누적 합도 출력하시오.
'''
import random
arr = []
cnt = 0
sum = 0
for i in range(5) :
    randNumber = random.randint(100, 200)
    arr.append(randNumber)
print("arr = ", arr)

for i in range(len(arr)) :
    checkingMultiple_3 = arr[i] % 3 == 0
    if checkingMultiple_3 :
        cnt += 1
        sum += arr[i]
print("3의 배수들의 합 = ", sum)
print("3의 배수들의 개수 = ", cnt)