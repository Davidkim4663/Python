'''
	[문제]
		1부터 100 사이의 랜덤 숫자를 변수 a에 저장한다.
		a의 값이 1부터  5   사이이면,  num에 1을  저장한 후 출력하시오.
		a의 값이 6부터  10  사이이면,  num에 6을  저장한 후 출력하시오.
		a의 값이 11부터 15  사이이면,  num에 11을 저장한 후 출력하시오.
		a의 값이 16부터 20  사이이면,  num에 16을 저장한 후 출력하시오.
		...
		...
		a의 값이 96부터 100 사이이면,  num에 96을 저장한 후 출력하시오.
'''
import random
randNum = random.randint(1, 100)
print("randNum = " + str(randNum))
# 5로 나눴을 때 나머지가 0이면 1로 저장, 나머지가 0이 아니면 6으로 저장

zero_value = randNum % 5 == 0
page = 0
if zero_value : page = randNum - 5 + 1
else : page = randNum - (randNum % 5) + 1
print(page)