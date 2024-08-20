'''
    [문제]
        1부터 10 사이의 랜덤 숫자 두 개를 출력한다.
        하나는 반드시 1~5 사이의 숫자이어야 하고,
        나머지 하나는 반드시 6~10 사이의 숫자이어야 한다.
        출력순서도 랜덤으로 출력되어야 한다.

        [예1]
            3, 6
        [예2]
            8, 1
'''

import random

oneNumber = random.randint(1, 10) # 1 ~ 5
otherNumber = random.randint(1, 10) # 6 ~ 10

switch = random.randint(1, 2)

if switch == 1: print(oneNumber, otherNumber)
else: print(otherNumber, oneNumber)