'''
	[문제1]
		a리스트의 값들을 한 칸씩
		앞으로 당기고 출력하시오.
	[정답1]
		a = [10,20,30,40,50,0]


'''

# [문제1]
a = [0, 10, 20, 30, 40, 50]
print("변경 전 [a] = ",a)
"""
a[0] = a[1] => a[0] = 10
a[1] = a[2] => a[1] = 20
a[2] = a[3] => a[2] = 30
a[3] = a[4] => a[3] = 40
a[4] = a[5] => a[0] = 50
a[5] ???
"""
temp = a[0]
for i in range(len(a) - 1) :
    a[i] = a[i + 1]
lastIndex = len(a) - 1
a[lastIndex] = temp
print("변경 후 [a] = ",a)
"""
	[문제2]
		b리스트의 값들을 한 칸씩
		뒤로 밀고 출력하시오.
	[정답2]
	         [10,20,30,40,50,0]
		b =  [0,10,20,30,40,50]
"""
b = [10, 20, 30, 40, 50, 0]
tempBox = b[0]

lastBox = b[len(b) - 1]

index = len(b) - 1
for i in range(len(b) - 1) :
    b[index] = b[index - 1]
    index -= 1

b[0] = 0
print(b)
