'''
    [문제]
        a의 값들을 거꾸로 출력하시오.
    [정답]
        60 54 12 44 21
        a[0] - a[4] - a[0] - 21
        a[1] - a[3] - a[1] - 44
        a[2] - a[2] - a[2] - 12
        a[3] - a[1] - a[3] - 56
        a[4] - a[0] - a[3] - 60
'''
a = [21, 44, 12, 54, 60]
print("정렬 before = ", a)

index = len(a) - 1
for i in range(len(a)) :
    print(a[index],end=" ")
    index -= 1