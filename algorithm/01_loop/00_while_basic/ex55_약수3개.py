'''
	[문제]
		어떤 수를 1부터 자기 숫자까지 나눠서 나눠지는 수를 약수라고 한다.
		랜덤으로 1~100을 저장 후,
		약수가 3개이면 "정답"을
		아니면 "오답"을 출력하시오.
'''
import random
from random import randint

divisor = random.randint(1, 100)
print("약수 = " , divisor,"\n")
# 권유남
i = 1
cnt = 0
while True :
    checkingDivisor = divisor % i == 0
    if checkingDivisor :
        print(i,end= " ")
        cnt += 1
        if cnt == 3 :
            break

    i += 1
if cnt == 3 : 
    print("정답")
elif cnt <= 3 :
    print("오답")
