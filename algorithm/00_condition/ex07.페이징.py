'''
[문제]
	1~200 사이의 랜덤숫자를 저장하고 다음과 같이 출력하시오.

	랜덤 숫자가
	1~10 	사이 값이면, 1
	11~20	사이 값이면, 11
	21~30	사이 값이면, 21
	......
	101 ~ 110 사이 값이면, 101

	[예]
		5   ==> 1
		10  ==> 1
		11  ==> 11
		20  ==> 11
		24  ==> 21
		30  ==> 21
		104 ==> 101
		154 ==> 151
'''
import random
randNum = random.randint(1, 200)
print("randon = " + str(randNum))

page = 0
# 10으로 나눠서 몫이 0인 경우 10, 20, 30 etc
if randNum % 10 == 0: page = randNum - 10 + 1;
else: page = randNum - (randNum % 10) + 1
print(page)