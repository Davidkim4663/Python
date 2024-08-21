'''
	[문제]
		[조건1] 18의 약수 중 짝수들만 출력하고,
     	[조건2] 총합을 출력하시오.
		[조건3] 개수를 구하시오.
	[정답]
		2 6 18
		total = 26
		count = 3
'''
sum = 0
cnt = 0
divisor = 18
i = 1
while i <= divisor :
    checking_divisor = divisor % i == 0 and i % 2 == 0
    if checking_divisor :
        print(i, end=" ")
        sum+=i
        cnt += 1
    i += 1
print()
print("sum = ", sum)
print("cnt = ", cnt)