'''
    [문제]
        a 리스트에서 백의자리가 2인 수만 출력하시오.
    [정답]
        1210
        1212
'''

a = [1210, 1343, 1524, 1212, 7452]
print("a = ", a, end=" ")
print()
for i in range(len(a)) :
    checking_hundred_unit = (a[i] % 1000) // 100 == 2
    if checking_hundred_unit :
        print(a[i])
