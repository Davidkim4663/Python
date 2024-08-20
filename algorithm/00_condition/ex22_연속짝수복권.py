'''
[문제]
	100~900 사이의 랜덤숫자를 출력한다.
	세 자리의 숫자를 전부 한 자리씩 분리한다.
	[규칙]
		[1] 세 자리 모두 짝수이면 "1등"을 출력한다.
		[2] 두 자리가 짝수이고, 짝수인 숫자가 연속이면 "2등"을 출력한다.
		[3] 그 외는 "꽝"을 출력한다.
		[4] 단, 0은 짝수이다.
		[예]
			462 ==> 4,6,2 세 자리 모두 짝수이므로 ==> 1등
			245 ==> 2,4,5 두 자리가 짝수이고 2, 4연속이므로 ==> 2등
			456 ==> 4,5,6 두 자리가 짝수이지만 연속이 아니므로 ==> 꽝
			782 ==> 7,8,2 두 자리가 짝수이고 8, 2연속이므로 ==> 2등
'''
import random
randomNumber = random.randint(100, 900)

# 자리수 분리
unit_hundred = randomNumber // 100
unit_ten = (randomNumber % 100 ) // 10
unit_one = randomNumber % 10
print(str(unit_hundred) + ", " + str(unit_ten) + ", " + str(unit_one))

# 1등
triple_even = unit_hundred % 2 == 0 and unit_ten % 2 == 0 and unit_one % 2 == 0 
firstClass = triple_even

#2등
double_even_one = (unit_hundred % 2 == 0 and unit_ten % 2 == 0) and unit_one % 2 != 0
double_even_other = unit_hundred % 2 != 0 and (unit_ten % 2 == 0 and unit_one % 2 == 0)

# 꼴지
secondClass = double_even_one or double_even_other
fall = not firstClass and not secondClass

str = ""
if firstClass : str = "1등"
elif secondClass : str = "2등"
elif fall : str = "꽝"
print(str)