'''
	[문제]
		철수는 무인도를 사들여 국왕이 되었다.
		철수는 평소 월요일을 싫어해서 주 7일을 주 6일로 바꾸고 월요일을 삭제했다.
		5월 1일이 일요일이면,
		5월 1일부터 5월31일까지 날짜와 요일을 전부 출력해보자.
		[예시]
			1 일
			2 화
			3 수
			4 목
			5 금
			6 토
			7 일
			8 화
			9 수
			10 목
			...
			22 목
			23 금
			24 토
			25 일
			26 화
			...
			30 토
			31 일
'''
i = 1
endMonth = 31
dayStr = " "
while i <= endMonth :
    week = i % 6
    sunday = week == 1
    tuesday = week == 2
    wendsday = week == 3
    thursday = week == 4
    friday = week == 5
    saturday = week == 0
    if sunday :
        dayStr = "일요일"
    elif tuesday :
        dayStr = "화요일"
    elif wendsday :
        dayStr = "수요일"
    elif thursday :
        dayStr = "목요일"
    elif friday :
        dayStr = "금요일"
    elif saturday :
        dayStr = "토요일"
    print(i, end=f" {dayStr}\n")
    i += 1
