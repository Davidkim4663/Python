'''
    [문제]
        a 리스트에서 일의자리가 2인 수만 출력하시오.
    [정답]
        12
        52
'''

a = [10,43,24,12,52]
print("a = ", a, "\n")
for i in range(len(a)) :
    checkingUnit_one = a[i] % 10 == 2
    if checkingUnit_one :
        print(a[i])