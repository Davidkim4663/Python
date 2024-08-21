'''
	[문제]
	  	120의 약수 중에서 순서대로 약수를 출력했을 때,
        일의자리가 4인 약수들만 출력하시오.
	[정답]
		4
		24
'''
divisor = 120
i = 1
while i <= divisor :
    checking_divisor = divisor % i == 0
    checking_unit = i % 10 == 4
    checking_total = checking_divisor and checking_unit
    if checking_total : print(i)
    i += 1