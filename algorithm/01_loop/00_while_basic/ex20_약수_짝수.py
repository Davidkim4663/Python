'''
	[문제]
		48의 약수 중 짝수만 출력하시오.
	[정답]
		2
		4
		6
		8
		12
		16
		24
		48
'''
divisor = 48
i = 1
while divisor >= i:
    checking_divisor = divisor % i == 0 and i % 2 == 0
    if checking_divisor : print(i)
    i += 1