'''
	[문제]
	  	120의 약수 중에서 순서대로 약수를 출력했을 때,
        일의자리가 4인 두 번째 약수를 출력하시오.
	[정답]
		24
'''
divisor = 120
i = 1
cnt = 0
while i <= divisor:
    checkingDivisor = divisor % i == 0
    checkingUnit_one = i % 10 == 4
    checkingTotal = checkingDivisor and checkingUnit_one
    if checkingTotal :
        cnt += 1
        if cnt == 2 :
            print(i)
    i += 1

