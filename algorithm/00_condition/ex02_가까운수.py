import random
'''
    [문제]
        a는 1~9 사이의 랜덤 숫자를 저장한다.
        c는 11~20 사이의 랜덤 숫자를 저장한다.
        a와 c 중 어떤 숫자가 b와 더 가까운지 출력하시오.

        [1] a가 c보다 가까우면 "a가 가깝다."
        [2] c가 a보다 가까우면 "c가 가깝다."
        [3] 서로 거리가 같으면 "서로 같다."
'''

numberSmall = random.randint(1, 9)
numberBig = random.randint(11, 20)
b = 10

print("a = " + str(numberSmall))
print("c = " + str(numberBig))

calc_small = b - numberSmall;
calc_big = numberBig - b;
print("calc_small = " + str(calc_small))
print("calc_big = " + str(calc_big))

calc_checking_small = calc_small < calc_big # small이 더 범위가 좁을 때
calc_checking_big = calc_small > calc_big # big  더 범위가 좁을 때

if calc_checking_small: print("a가 더 가깝다")
elif calc_checking_big: print("b가 더 가깝다")
else: print("서로 같다")
