'''
    [문제]
        [1] 1~50까지 반복한다.
        [2] 3이나 6이나 9가 없는 수 중 짝수만 a리스트에 추가하시오.
    [정답]
        a = [2, 4, 8, 10, 12, 14, 18, 20, 22, 24, 28, 40, 42, 44, 48, 50]
'''
a = []

for i in range(1, 50 + 1) :
    unit_ten = i // 10
    unit_one = i % 10
    checking_unit_double = unit_ten == 3 or unit_ten == 6 or unit_ten == 9
    checking_unit_one = unit_one == 3 or unit_one == 6 or unit_one == 9

    unit_double = checking_unit_double and checking_unit_one
    unit_one = checking_unit_double or checking_unit_one

    exceptCondition = not unit_double and not unit_one
    unit_even = i % 2 == 0
    join_condition_total = exceptCondition and unit_even
    if join_condition_total :
        a.append(i)

print("a = ", a)