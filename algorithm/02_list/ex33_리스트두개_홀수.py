'''
    [문제]
        a리스트와 b리스트에 랜덤 숫자(1~100)를 다섯 개씩 저장하고,
        a리스트의 전체 합과 b리스트의 홀수의 합을 출력하시오.
        a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
        서로 같으면 둘 다 출력하시오.
    [예시]
        a = [28, 79, 47, 70, 36]
        b = [63, 4, 45, 54, 87]
        total1 = 126
        total2 = 195
        195
'''
import random

a = []
b = []
total_a = 0
total_a_odd = 0
total_b = 0
total_b_odd = 0

for i in range(5):
    randNumber_a = random.randint(1, 100)
    randNumber_b = random.randint(1, 100)
    a.append(randNumber_a)
    b.append(randNumber_b)
print("a = ", a)
print("b = ", b)
print()
#  a 리스트의 전체 합과 b 리스트의 "홀수의 합"
print("b 리스트의 홀수 = ", end=" ")
for i in range(len(a)):
    total_a += a[i]
    # b 리스트의 홀수 합
    checking_odd = b[i] % 2 != 0
    if checking_odd:
        print(b[i], end=" ")
        total_b_odd += b[i]
print()
print("total_a = ", total_a)
print("[홀수]total_b = ", total_b_odd)
print()
print("a 리스트의 홀수 = ", end=" ")
for i in range(len(b)):
    total_b += b[i]
    # a 리스트의 홀수 합
    checking_odd = a[i] % 2 != 0
    if checking_odd:
        print(a[i], end=" ")
        total_a_odd += a[i]
print()
print("total_b = ", total_b)
print("[홀수]total_a = ", total_a_odd)
print()
#   a리스트의 홀수 합과 b리스트의 홀수 합을 비교해서 더 큰 값을 출력하시오.
comparison_total_A = total_a_odd > total_b_odd
comparison_total_B = total_b_odd > total_a_odd
comparison_total_same = total_b_odd == total_a_odd
if comparison_total_A:
    print("a 리스트 홀수의 총합이 더 크다, ", total_a_odd)
elif comparison_total_B:
    print("b 리스트 홀수의 총합이 더 크다, ", total_b_odd)
elif comparison_total_same :
    print("a 리스트 홀수의 합과 b 리스트 홀수의 합은 서로 같다, ", total_a_odd, ",",total_b_odd)