'''
	[1] 비교연산자를 활용해 짝수 , 홀수 판별법
		(1) 짝수 : 2의 배수이면 짝수
		(2) 홀수 : 2의 배수가 아니면 홀수
 		(3) 2의 배수 : 어떤수를 2로나눴을때 나머지가 0 이면 2의배수
  		(4) 3의 배수 : 어떤수를 3으로나눴을때 나머지가 0 이면 3의 배수
'''
import random
from random import randint
number = random.randint(1, 6) # 1 ~ 6의 정수 랜덤값
print("randNum = " + str(number) + "\n")

odd = number % 2 != 0 # 문자열과 정수를 같이 사용하려면 내장함수 str()를 사용해야한다.
print("odd = " + str(odd))

even = number % 2 == 0
print("even = " + str(even))
