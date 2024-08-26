'''
    [문제]
        [조건1] 리스트 두 개에 1~100 사이의 랜덤 값 다섯 개를 저장한다.
        [조건2] 둘 다 짝수이거나 "짝수" 출력, 둘 다 홀수이면 "홀수" 출력 ,
                한쪽은 홀수이고 다른 한쪽은 짝수이면 "다르다"를 출력하시오.
    [예시]
        a = [48, 71, 66, 85, 65]
        b = [99, 81, 75, 24, 40]
        다르다
        홀수
        다르다
        다르다
        다르다
'''
import random
a = []
b = []
for i in range(5) :
    randNum_a = random.randint(1, 100)
    randNum_b = random.randint(1, 100)
    a.append(randNum_a)
    b.append(randNum_b)
print("a = ", a)
print("b = ", b)

for i in range(len(a)) :
    checkingEven = a[i] % 2 == 0 and b[i] % 2 == 0
    checkingOdd = a[i] % 2 != 0 and b[i] % 2 != 0
    checkingNot = not checkingEven and not checkingOdd
    
    if checkingEven :
        print(a[i],",",b[i], " >> 짝수")
    elif checkingOdd :    
        print(a[i],",",b[i], " >> 홀수")
    elif checkingNot :
        print(a[i],",",b[i], " >> 다르다")
