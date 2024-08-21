'''
	[문제]
		1000의 약수 중에서 200~800 사이 중에서
		십의자리가 5인 수만 출력하시오.
	[정답]
		250
'''
divisor = 1000
i = 1
while i <= divisor:
    checking_divisor = (divisor % i == 0 and 200 <= i <= 800) and ((i % 100) // 10 == 5)
    checking_divisor_scope_total = checking_divisor
    if checking_divisor_scope_total : print(i)
    i += 1