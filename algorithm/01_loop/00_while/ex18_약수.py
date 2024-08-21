'''
	[문제]
	    18의 약수를 출력하시오.
	[정답]
		1
		2
		3
		6
		9
		18
'''
divisor = 18
i = 1
while divisor >= i:
    if divisor % i == 0 : print(i)
    i += 1
