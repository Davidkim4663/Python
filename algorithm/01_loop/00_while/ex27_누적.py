'''
	[문제]
		[조건1]  30의 약수를 출력하고
  		[조건2]  전체 합을 구하시오.
		[조건3]  개수를 구하시오.

	[정답]
		1 2 3 5 6 10 15 30
		total = 72
		count = 8
'''
sum = 0
cnt = 0
divisor = 30
i = 1
while i <= divisor :
    checking_divisor = divisor % i == 0
    if checking_divisor :
     print(i, end=" ")
     cnt += 1
     sum += i
    i+= 1

print()
print("sum = " ,sum)
print("cnt = " ,cnt)