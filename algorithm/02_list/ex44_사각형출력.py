'''
	[문제]
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		1 2 3
		4 5 6
		7 8 9
'''
# 
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("a = ", a)
for i in range(len(a)):
    print(a[i], end=" ")
    if i % 3 == 0:
        print()
