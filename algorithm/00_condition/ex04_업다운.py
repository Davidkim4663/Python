'''
    [문제]
        1부터 100 사이의 숫자 두 개를 랜덤으로 저장한다.
        두 숫자 중 더 큰 숫자를 출력하시오.
        단, 서로 같으면 "같다"를 출력하시오.
'''
import random
oneNumber = random.randint(1, 100)
otherNumber = random.randint(1, 100)
big = 0
print("oneNumber = " + str(oneNumber))
print("otherNumber = " + str(otherNumber) + "\n")


oneNumber_big = oneNumber > otherNumber
otherNumber_big = oneNumber < otherNumber

if oneNumber_big: big = oneNumber
elif otherNumber_big: big = otherNumber
else:print("서로 같다")

result = big
print("result = " + str(result))

