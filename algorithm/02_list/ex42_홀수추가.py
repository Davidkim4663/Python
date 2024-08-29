'''
	[문제]
		다음 리스트를 이용해서 a의 값 중
		홀수만 b에 저장하고 출력하시오.
	[예]
 		b = [ 49, 51, 17 ]
'''
a = [49, 2, 51, 22, 17]
b = []
odd = 0
for i in range(len(a)) :
    checkingOdd = a[i] % 2 != 0
    odd = a[i]
    if checkingOdd :
        b.append(odd)

print("b = ", b)