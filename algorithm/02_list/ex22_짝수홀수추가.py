'''
	[문제]
		두 개의 변수 a, b에 숫자를 랜덤(1~9 사이의 숫자)으로 저장한다.
		두 변수 중 a 가 값이 더 크면 arr1 배열에 저장한다.
		b의 값이 더 크면 arr2 배열에 저장한다.
		앞에서부터 순차적으로 저장한다.
		만약에 값이 같으면 둘 다 저장한다.
		총 다섯 번을 반복하고 배열을 출력하시오.

		[예시]
            a = [4, 3, 8, 3, 7]
            b = [5, 4, 8, 9, 7]
            arr1 = [8, 7]
            arr2 = [5, 4, 8, 9, 7]
'''
import random
a = []
b = []
for i in range(5) :
    randNum_a = random.randint(1, 9)
    randNum_b = random.randint(1, 9)
    a.append(randNum_a)
    b.append(randNum_b)

print("a = ", a)
print("b = ", b)

arr1 = []
arr2 = []

for i in range(len(a)) :
    checking_Big_a = a[i] > b[i]
    if checking_Big_a :
        arr1.append(a[i])

    checking_Big_b = a[i] < b[i]
    if checking_Big_b :
        arr2.append(b[i])
print("arr1 = ", arr1)
print("arr2 = ", arr2)