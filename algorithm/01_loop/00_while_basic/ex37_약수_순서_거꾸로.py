'''
[문제]
	852의 약수 중에서 큰 수부터 작은 수를 거꾸로 출력했을 때,
	다섯 번째 약수만 출력하시오.
[정답]
	142
'''

number = 852
i = 852
cnt = 0
rs = i
while i >= 1:
    checkingDivisor = number % i == 0
    if checkingDivisor:
        print(i)
        cnt += 1
        if cnt == 5 :
            rs = i
            break
    i -= 1
print()
print("rs = ", rs)
