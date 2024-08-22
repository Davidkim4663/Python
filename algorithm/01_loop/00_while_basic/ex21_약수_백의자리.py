'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때,
        백의자리가 4인 약수들만 출력하시오.
	[정답]
		495
'''
divisor = 1980
i = 1
while i <= divisor :
    checking_divisor_unit = divisor % i == 0
    unit_hundred = (i % 1000) // 100 == 4
    join_checking = checking_divisor_unit and unit_hundred
    if join_checking : print(i)
    i += 1