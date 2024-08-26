'''
    [문제]
        a 리스트에서 십의자리가 1이고, 백의자리가 5인 수만 출력하시오.
    [정답]
        510
        512
'''

a = [510,423,124,512,252,23,312,453,122]

for i in range(len(a)) :
    checkingUnit_hundred = a[i] // 100 == 5
    checkingUnit_ten= (a[i] % 100) // 10  == 1
    checkingUnit_Total = checkingUnit_hundred and checkingUnit_ten
    if checkingUnit_Total :
        print(a[i])