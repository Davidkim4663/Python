'''
	[문제]
	  	745의 약수 중에서 작은 수부터 출력했을 때,
		세 번째 약수만 출력하시오.
	[정답]
		149
'''
divisor = 745
i = 1
cnt = 0
while i <= divisor :
    checkingDivisor = divisor % i == 0
    if checkingDivisor :
        cnt += 1
        if cnt == 3 :
            print(i)
    i += 1