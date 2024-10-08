'''
[문제]
    100 이상인 9의 배수 중에서
    10의 자리가 6인 두 번째 배수를 출력하시오.
[정답]
    261
[설명]
    배수는 범위를 특별히 제한하지 않으면 계속해서 커지기 때문에,
    위 문제를 풀기 위해선 무한 반복문을 사용해야 한다.

'''
i = 100
cnt = 0
while True :
    multiple_9 = i % 9 == 0
    checkingUnit = i % 100 // 10 == 6
    joiningCondition = multiple_9 and checkingUnit
    if joiningCondition :
        cnt += 1
        if cnt == 2 :
            print(i)
            break
    i += 1
