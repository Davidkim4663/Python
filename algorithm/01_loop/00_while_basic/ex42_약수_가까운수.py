'''
	[문제]
		200의 약수 중에서 짝수 중
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''
divisor = 200
i = 1
cnt = 0
while True :
    checkingDivisor = divisor % i == 0
    if checkingDivisor :
        nearNumber = i >= 80
        if nearNumber :
            cnt += 1
            if cnt == 1 :
                print(i)
    i += 1