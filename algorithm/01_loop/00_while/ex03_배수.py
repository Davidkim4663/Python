'''
[문제] 아래 조건을 만족하는 식을 작성하시오.
		[조건1] 1~10까지 반복문을 활용해서 숫자를 출력한다.
		[조건2] 위 숫자 중 3의 배수일 때는 "삼의 배수"를 출력한다.
[정답]
	1
	2
	삼의배수
	4
	5
	삼의배수
	7
	8
	삼의배수
	10
'''
i = 1
while i <= 10:
     if i % 3 == 0 :
         print("삼의배수")
     else : print(i)
     i += 1