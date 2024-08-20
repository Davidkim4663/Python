'''
[문제]
	[1] 1~99 사이의 랜덤 숫자를 저장한다.

	랜덤 숫자 중에서 3이나 6이나 9의 개수가
	[2-1] 2개이면, 짝짝을 출력한다.
	[2-2] 1개이면, 짝을 출력한다.
	[2-3] 0개이면, 해당 숫자를 출력하시오.

	[예]
		33	==> 짝짝
		16	==> 짝
		 7	==> 7
'''
import random

randNum = random.randint(1, 99)
print("randNum = " + str(randNum) + "\n")
# 십의 자리가 3,6,9 일때
unit_ten = (randNum // 10 == 3) or (randNum // 10 == 6) or (randNum // 10 == 9) # 짝짝
unit_one = (randNum % 10 == 3) or (randNum % 10 == 6) or (randNum % 10 == 9) # 짝

double_clab = unit_ten and unit_one
single_clab = unit_ten or unit_one
none_clab = not unit_ten and not unit_one
if double_clab : print("짝짝")
elif single_clab : print("짝")
elif none_clab : print(randNum)
