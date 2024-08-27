'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 리스트의 숫자중 50보다 큰값들만 출력
        [조건3] 위조건의 값들의 누적합을 출력
        [조건4] 위조건의 개수 출력

    [예시]
        a = [1, 83, 22, 77 ,19]
        비교 = 50
        출력 : 83, 77
        합 : 160
        개수 : 2
'''
import random
a = []
comparsion = 0
sum = 0
cnt = 0
for i in range(5) :
    randNumber = random.randint(1, 100)
    a.append(randNumber)
print("a = ", a)
print("비교 : ", 50, end="\n출력 >> ")
for i in range(len(a)) :
    bigNumber_50 = a[i] > 50
    if bigNumber_50 :
        print(a[i], end=" ")
        sum += a[i]
        cnt += 1
print()
print("합계 : ", sum)
print("개수 : ", cnt)