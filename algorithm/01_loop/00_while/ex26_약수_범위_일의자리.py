'''
	[문제]
		1000의 약수 중에서 200~800 사이 중에
		일의자리가 0인 수만 출력하시오.
	[정답]
		200
		250
		500
'''
divisor = 1000
i = 1
while i <= divisor :
    checking_divisor_unit = (divisor % i == 0) and (200 <= i <= 800) and (i % 10) == 0
    if checking_divisor_unit : print(i)
    i += 1