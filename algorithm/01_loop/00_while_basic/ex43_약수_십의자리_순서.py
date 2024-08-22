'''
	[문제]
	  	1980의 약수 중에서 순서대로 약수를 출력했을 때,
        십의자리가 3인 두 번째 약수를 출력하시오.
	[정답]
		33
'''
divisor = 1980
i = 1
cnt = 0
while i <= divisor:
    checkingDivisor = divisor % i == 0 # 약수 확인
    checkingUnit = i % 100 // 10 == 3 # 십의자리가 3
    checkingTotal = checkingDivisor and checkingUnit
    if checkingTotal :
     cnt += 1
     if cnt == 2 :
         print(i)
    i += 1