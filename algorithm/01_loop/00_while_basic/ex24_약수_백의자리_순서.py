'''
[문제]
	1980의 약수 중에서 순서대로 약수를 출력했을 때,
	십의 자리가 9인 두 번째 약수를 출력하시오.
[정답]
	99
'''
divisor = 1980
i = 1
cnt = 0
while i <= divisor:
    checkingDivisor = divisor % i == 0
    checkingUnit = i % 100 // 10 == 9
    joinCondition = checkingDivisor and checkingUnit
    if joinCondition:
        cnt += 1
        if cnt == 2:
         print(i)
    i += 1
