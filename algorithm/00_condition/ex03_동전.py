'''
    [문제]
        동전의 앞과 뒤를 랜덤숫자 0 또는 1로 표현한다.
        동전 두 개를 던져서 둘 다 "앞"이면 "정답",
        둘 다 "뒤"이어도 "정답"이다.
        둘 중 하나라도 반대면 "꽝"을 출력하시오.
'''
import random

coin_one = random.randint(0,1)
coin_another = random.randint(0,1)

print("coin_one = " + str(coin_one))
print("coin_another = " + str(coin_another))

checking_coin_front = (coin_one == 0 and coin_another == 0) or (coin_one == 1 and coin_another == 1)

if checking_coin_front:print("정답")
else:print("꽝")




