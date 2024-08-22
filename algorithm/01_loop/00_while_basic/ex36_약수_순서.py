'''
[문제]
	75의 약수 중에서 작은 수부터 큰 수를 출력했을 때,
	다섯 번째 약수만 출력하시오.
[정답]
	25
'''
divisor = 75
i = 1
cnt = 0
rs = 0
while i <= divisor :
    checkingDivisor = divisor % i == 0
    if checkingDivisor :
        print(i)
        cnt += 1
        if cnt == 5 :
            rs = i
            break
    i += 1
print()
print("rs = " , rs)