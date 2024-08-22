'''
[문제]
    100 이상인 7의 배수 중
    3개만 차례대로 출력하시오.
[정답]
    105
    112
    119
[설명]
    배수는 범위를 특별히 제한하지 않으면 계속해서 커지기 때문에,
    위 문제를 풀기 위해선 무한 반복문을 사용해야 한다.
'''
i = 100
cnt = 0
while True:
    checking_Scope = i % 7 == 0
    if checking_Scope:
        print(i)
        cnt += 1
        if cnt == 3:
            break
    i += 1
