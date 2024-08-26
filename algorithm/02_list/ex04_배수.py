'''
    [문제]
        a 리스트에서 3의 배수만 출력하시오.
    [정답]
        24
        12
'''

a = [10, 43, 24, 12, 52]
print("a = ", a)
print()

multiple_3 = 0
for i in range(len(a)) :
    Checking_multiple_3 = a[i] % 3 == 0
    if Checking_multiple_3 :
        multiple_3 = a[i]
        print("3의 배수 = ", multiple_3)
