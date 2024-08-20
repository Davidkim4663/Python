'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (1~1000 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 큰 수(MAX)를 출력한다.
'''

import random
firstNumber = random.randint(1, 1000)
secondNumber = random.randint(1, 1000)
thirdNumber = random.randint(1, 1000)
print(str(firstNumber) + ", " + str(secondNumber) + ", " + str(thirdNumber) )

max_first = (firstNumber > secondNumber) and (firstNumber > thirdNumber)
max_second = (secondNumber > firstNumber) and (secondNumber > thirdNumber)
max_third = (thirdNumber > firstNumber) and (thirdNumber > secondNumber)

max = 0
if max_first : max = firstNumber
elif max_second : max = secondNumber
elif max_third : max = thirdNumber
print("max = " + str(max))