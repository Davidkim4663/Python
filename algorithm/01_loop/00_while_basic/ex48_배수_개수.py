'''
	[문제]
		[1] 100 이상의 숫자 중에서
			7의 배수를 순차적으로 검색한다.
		[2] 작은 수부터 순차적으로 다섯 개를 출력하시오.
	[정답]
		105 112 119 126 133
'''
i = 100
cnt = 0
while True :
    checkingMultiple = i % 7 == 0
    if checkingMultiple :
        print(i,end=" ")
        cnt+= 1
        if cnt == 5 :
            break
    i += 1