'''
	[문제]
		[1] 10000~90000 사이의 랜덤 숫자 저장한다.
		[2] 두 번째 자리와 네 번째 자릿수의 합을 출력하시오.

		[예]
			랜덤숫자 : 45343

			두 번째 자릿수 : 5
			네 번째 자릿수 : 4
			합 : 9
'''
import random
randNum = random.randint(10000, 90000)
print("randNum = " + str(randNum))

unit_hundred = (randNum % 10000) // 1000
unit_ten = (randNum % 100) // 10
print("두 번째 자릿수 = " + str(unit_hundred))
print("네 번째 자릿수 = " + str(unit_ten))

unit_sum = unit_hundred + unit_ten
print("sum = " + str(unit_sum))