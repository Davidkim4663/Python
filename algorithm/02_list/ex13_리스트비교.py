'''
    [문제]
        리스트 a와 리스트 b에 랜덤 숫자(1~10) 다섯 개씩 저장한다.
        a와 b를 각각 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
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
print()
for i in range(len(a)) :
    comparsion_big_a = a[i] > b[i]
    comparsion_big_b = a[i] < b[i]
    comparsion_same = a[i] == b[i]
    if comparsion_big_a :
        print("a가 더 크다 ", a[i])
    elif comparsion_big_b :
        print("b가 더 크다 ", b[i])
    elif comparsion_same :
        print("서로 같다, a = ",a[i], "\nb = ", b[i])
