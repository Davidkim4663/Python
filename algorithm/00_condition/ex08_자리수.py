'''
[자리수]
	[1] 10000~90000 사이의 랜덤 숫자 저장한다.
	[2] 랜덤 숫자의 백의자리 숫자를 출력하시오.
	[예]
		[랜덤] ==> 24912
		[출력] ==> 9
'''
import random
randNum = random.randint(10000, 90000)
print("[랜덤] : " + (str)(randNum))

hundredPos = ((randNum % 1000) // 100)
print("[출력] : " + (str)(hundredPos))

