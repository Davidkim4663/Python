'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 전체 합 중 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [93, 100, 41, 74, 45]
        b = [84, 80, 25, 19, 27]
        total1 = 353
        total2 = 235
        353
'''
import random
a = []
b = []
total_a= 0
total_b= 0

for i in range(5) :
    randNumber_a = random.randint(1, 100)
    randNumber_b = random.randint(1, 100)
    a.append(randNumber_a)
    b.append(randNumber_b)
print("a = ", a)
print("b = ", b)

for i in range(len(a)) :
    total_a += a[i]
    total_b += b[i]

print("total_a = ",total_a)
print("total_b = ",total_b)

comparison_total_A = total_a > total_b
comparison_total_B = total_a < total_b
if comparison_total_A :
    print("a 배열의 총합이 더 크다, ", total_a)
elif comparison_total_B :
    print("b 배열의 총합이 더 크다, ", total_b)
