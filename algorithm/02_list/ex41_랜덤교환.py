'''
	[문제]
		랜덤으로 리스트의 값을 교환하고, 출력하시오.
	[예시]
		교환 전  [10,20,30,40,50,60,70,80] : 30과 40을 교환
		교환 후  [10,20,40,30,50,60,70,80]
'''
import random

a = [10, 20, 30, 40, 50, 60, 70, 80]
print("교환 전 =", a)

idx1 = random.randint(0, len(a) - 1)
idx2 = random.randint(0, len(a) - 1)
print("idx1", idx1)
print("idx2", idx2)

temp = 0
temp = a[idx1] #temp 10
a[idx1] = a[idx2]
a[idx2] = temp
print("교환 후 =", a)
