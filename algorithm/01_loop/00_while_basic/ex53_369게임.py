'''
[문제]
    1. 1~50까지 반복한다.
    2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
    3. 각각의 숫자에 3이나 6이나 9가 두 개면 "짝짝"
    4. 각각의 숫자에 3이나 6이나 9가 한 개면 "짝"
    5. 3이나 6이나 9가 없으면 그냥 숫자를 출력하시오.

[결과]
    1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...
'''
i = 1
while i <= 50 :
    checking_unit_ten = i // 10 == 3 or i // 10 == 6 or i // 10 == 9
    checking_unit_one = i % 10 == 3 or i % 10 == 6 or i % 10 == 9
    clap_twice = checking_unit_ten and checking_unit_one # 33,, 36, 39
    clap_once = checking_unit_ten or checking_unit_one # 30 31, 23 etc
    if clap_twice : print("짝짝")
    elif clap_once : print("짝")
    else : print(i)
    i += 1
