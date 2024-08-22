'''
	[문제]
		9의 배수 중 십의 자리가 6인
		다섯 번째 배수를 출력하시오.
	[정답]
		369
'''
i = 1
cnt = 0
while True :
    checkingMultiple = i % 9 == 0
    checkingUnit = i % 100 // 10 == 6
    checkingTotal = checkingMultiple and checkingUnit
    if checkingTotal :
        cnt += 1
        if cnt == 5 :
            print(i)
            break
    i += 1