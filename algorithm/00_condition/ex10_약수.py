'''
  [문제]
    변수에 1부터 10 사이의 숫자를 랜덤으로 저장한다.
    저장한 숫자의 값이 300의 약수이면 "True"
    300의 약수가 아니면 "False" 출력하시오.
'''
import random
divisor = 300
randNum = random.randint(1, 10)
checking_Divisor = divisor % randNum == 0
print("300의 약수  = " + str(divisor) + ", randNum = " + str(randNum) + ", " + str(checking_Divisor))
if checking_Divisor : print(True)
else : print(False)