'''
	[문제]
		100의 약수 중에서
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''
i = 1
divisor = 100
cnt = 0
Pos_two = 0
Pos_Five = 0
while i <= divisor :
    checkingDivisor = divisor % i == 0
    if checkingDivisor :
        print(i)
        cnt += 1
        if cnt == 2 :
            Pos_two = i
        if cnt == 5 :
            Pos_Five = i
    i += 1
print()
print("5번째 약수 = ", Pos_Five)
print("2번째 약수 = ", Pos_two)

divisorsMinus = Pos_Five - Pos_two
print("rs = ", divisorsMinus)