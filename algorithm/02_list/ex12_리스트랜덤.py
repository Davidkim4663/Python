'''
    [문제]
        리스트a 와 리스트b 에 랜덤 숫자(1~10) 다섯 개씩 저장하고,
        둘 다 출력하시오.
'''
import random
a = []
b = []

for i in range(5) :
    randNum_a = random.randint(1, 10)
    randNum_b = random.randint(1, 10)
    a.append(randNum_a)
    b.append(randNum_b)
print("a = ", a,end=" ")
print()
print("b = ", b,end=" ")