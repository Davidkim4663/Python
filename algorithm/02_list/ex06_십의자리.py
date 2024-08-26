'''
    [문제]
        a 리스트에서 십의 자리가 2인 수만 출력하시오.
    [정답]
        423
        124
        23
        122
'''

a = [510, 423, 124, 512, 252, 23, 312, 453, 122]
print("a = ",a)
print()
for i in range(len(a)) :
    checkingUnit_10 = (a[i] % 100) // 10 == 2
    if checkingUnit_10 :
        print(a[i], end=" ")
