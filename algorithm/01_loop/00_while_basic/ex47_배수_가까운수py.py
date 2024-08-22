'''
	[문제]
  		6의 배수를 순차적으로 검사한다.
  		그중 100에 가장 가까운 수를 출력하시오.
 	[정답]
		102
'''
i = 100
cnt = 0
while True :
    checkingMultiple = i % 6 == 0
    if checkingMultiple :
        cnt+= 1
        if cnt == 1 :
            print(i)
            break
    i += 1