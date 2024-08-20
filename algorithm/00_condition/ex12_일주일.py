'''
	[문제]
		이번 달 1일이 수요일이라고 할 때,
		랜덤으로 1~31을 저장하고 해당 요일을 출력하시오.

		[예]
		3일 ==> 금요일
		1일 수요일
		2일 목요일
		3일 금요일
		4일 토요일
		5일 일요일
		6일 월요일
		7일 화요일
		8일 수요일
		9일 목용ㄹ
		10
		11
		12

		    월      화      수      목      금      토      일
                    1       2       3       4       5
    6       7       8       9       10      11      12
    13      14      15      16      17      18      19
    20      21      22      23      24      25      26
    27      28      29      30      31
'''
import random
month = random.randint(1, 31)
week = 7

calc_days = month % week

print("month = " + str(month))

Friday = calc_days == 3
Saturday = calc_days == 4
Sunday = calc_days == 5
Monday = calc_days == 6
Tuesday = calc_days == 0
wendsday = calc_days == 1
Thurday = calc_days == 2

days =  ""
if Monday : days = "월요일"
elif Tuesday : days = "화요일"
elif wendsday : days = "수요일"
elif Thurday : days = "목요일"
elif Friday : days = "금요일"
elif Saturday : days = "토요일"
elif Sunday : days = "일요일"
print("days = " + days)