'''
[문제]
    280의 약수 중에
    50바로 전의 값과 바로 뒤의 값을 구하시오.
    만약 50이 약수이면, 바로 뒤의 값은 50이다.
[정답]
    40
    56
'''
divisor = 280
i = 1
front = 0
back = 0
cnt = 0
while i <= divisor :
    checking_divisor = divisor % i == 0
    if checking_divisor :
        print(i)
    #  i가 50이하 일 때
    if i < 50 :
        front = i
    if i >= 50 :
        cnt += 1
        if cnt == 1 :
            back = i
    i+=1
print()
print("front = ", front)
print("back = ", back)
