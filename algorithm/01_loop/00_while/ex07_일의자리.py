'''
[문제]
    100~300 사이의 숫자 중에서
    일의 자리의 숫자가 7이고
    십의 자리의 숫자가 3인 수만 출력하시오.
[정답]
    137
    237
'''
i = 100
while i <= 300 :
    unit_ten = (i % 100) // 10 == 3
    unit_one = i % 10 == 7
    unit_total = unit_ten and unit_one
    if unit_total : print(i)
    i += 1