'''
    [문제]
        행사참가자 번호가 100~300번까지 있다.
        그중에서 당첨 번호를 뽑으려고한다.
        당첨 번호는 아래의 규칙에 따라 당첨된다.
        [조건1] 8의 배수이면서 십의 자릿수가 2이다.
        [조건2] 9의 배수이면서 일의 자릿수가 5이다.
        당첨자의 번호만 출력하시오.
    [정답]
        120
        128
        135
        224
        225
'''
i = 100
while i <= 300:
    numberWining_one = (i % 8 == 0) and (i % 100 // 10 == 2)
    numberWining_other = (i % 9 == 0) and (i % 10 == 5)
    numberWining_total = numberWining_one or numberWining_other
    if numberWining_total : print(i)
    i += 1