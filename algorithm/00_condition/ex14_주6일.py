'''
	[문제]
		철수는 최근 무인도를 구입하고, 그 나라의 왕이 되었다.
		평소 월요병이 있던 철수는 일주일에서 월요일을 삭제하였다.
		만약 이번 달 1일이 일요일일 때, 랜덤으로 1~31을 저장하고,
		해당 날짜의 요일을 출력하시오.

		[예]
			1 : 일요일
			2 : 화요일
			3 : 수요일
			4 : 목요일
			5 : 금요일
			6 : 토요일
			7 : 일요일
			8 : 화요일
			...
'''
import random
month = random.randint(1, 31)
week = 6

calc_days = month % week
print("month = " + str(month))

Friday = calc_days == 5
Saturday = calc_days == 0
Sunday = calc_days == 1
Tuesday = calc_days == 2
wendsday = calc_days == 3
Thurday = calc_days == 4

days =  ""
if Tuesday : days = "화요일"
elif wendsday : days = "수요일"
elif Thurday : days = "목요일"
elif Friday : days = "금요일"
elif Saturday : days = "토요일"
elif Sunday : days = "일요일"
print("days = " + days)