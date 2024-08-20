'''
    [문제]
        변수에 1부터 100 사이의 랜덤 숫자를 저장한다.
        저장한 숫자의 값이 4의 배수이면 "True"
        4의 배수가 아니면 "False" 출력하시오.
'''
import random
randNum = random.randint(1, 100)
print("random = " + (str)(randNum) + "\n")

randNum_4 = randNum % 4 == 0
if randNum_4 : print("4의 배수 True")
else: print("4의 배수 아니므로 False")