'''
[최대값]
    [1] 숫자 3개를 랜덤으로 저장한다. (-100 ~ 100 사이의 숫자)
    [2] 3개의 랜덤 숫자를 비교한다.
    [3] 가장 작은 수(MIN)를 출력한다.
'''
import random
firstNumber = random.randint(-100, 100)
secondNumber = random.randint(-100, 100)
thirdNumber = random.randint(-100, 100)
print(str(firstNumber) + ", " + str(secondNumber) + ", " + str(thirdNumber) )

min_first = (firstNumber < secondNumber) and (firstNumber < thirdNumber)
min_second = (secondNumber < firstNumber) and (secondNumber < thirdNumber)
min_third = (thirdNumber < firstNumber) and (thirdNumber < secondNumber)

min = 0
if min_first : min = firstNumber
elif min_second : min = secondNumber
elif min_third : min = thirdNumber
print("min = " + str(min))