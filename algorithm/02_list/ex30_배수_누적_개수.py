'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 짝수만 출력하시오.
        [조건3] 짝수의 누적 합을 저장 후 출력하시오.
        [조건4] 짝수의 개수를 출력하시오.

    [예시]
        arr = [68, 81, 84, 72, 81]
        68
        84
        72

        개수 = 3
        합 = 224
'''
import random
sum = 0
cnt = 0
arr = []
for i in range(5) :
    randNumber = random.randint(1, 100)
    arr.append(randNumber)
print("arr = ", arr)

for i in range(len(arr)) :
    checkingEven = arr[i] % 2 == 0
    if checkingEven :
        print(arr[i])
        cnt += 1
        sum += arr[i]
print("개수 = ", cnt)
print("총합 = ", sum)
