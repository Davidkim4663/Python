'''
	[문제]
	    100~200 사이의 숫자 중에서
        [조건1] 6의 배수 중에서 일의 자리가 2인 수만 출력하고,
        [조건2] 그 합을 구하시오.
        [조건3] 그 개수를 구하시오.
    [정답]
        102 132 162 192
        total = 588
        count = 4
'''
sum = 0
cnt = 0
i = 100
while i <= 200:
    checking_multiples = i % 6 == 0 and i % 10 == 2
    if checking_multiples :
        print(i,end=" ")
        sum += i
        cnt += 1
    i+=1
print()
print("sum = ", sum)
print("cnt = ", cnt)