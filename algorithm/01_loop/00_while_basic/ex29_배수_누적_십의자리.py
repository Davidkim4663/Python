'''
	[문제]
	    100~200 사이의 숫자 중에서
        [조건1] 9의 배수 중에서 십의 자리가 7인 수만 출력하고,
        [조건2] 그 합을 구하시오.
        [조건3] 개수를 구하시오.
    [정답]
        171
        total = 171
        count = 1
'''
sum = 0
cnt = 0
i = 100

while i <= 200 :
    checking_divisor = i % 9 == 0 and (i % 100) // 10 == 7
    if checking_divisor :
        print(i, end=" ")
        sum += i
        cnt += 1
    i+= 1
print()
print("sum = ", sum)
print("cnt = ", cnt)