'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때,
        백의 자리가 3인 두 번째 약수를 출력하시오.
	[정답]
		396
'''
divisor = 1980
i = 1
cnt = 0

while i <= divisor :
    checkingDivisor = divisor % i == 0
    checkingUnit_100 = i % 1000 // 100 == 3
    checkingTotal = checkingDivisor and checkingUnit_100
    if checkingTotal :
        cnt += 1
        if cnt == 2 :
            print(i)
    i += 1