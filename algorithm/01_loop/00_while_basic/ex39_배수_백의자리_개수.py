'''
[문제]
    100 이상인 15의 배수 중
    백의 자리가 7인
    배수 3개만 차례대로 출력하시오.
[정답]
    705
    720
    735
[설명]
    배수는 범위를 특별히 제한하지 않으면 계속해서 커지기 때문에,
    위 문제를 풀기 위해선 무한 반복문을 사용해야 한다.
'''
i = 100
cnt = 0
while True :
    multiple_15 = i % 15 == 0
    unit_100 = i // 100 == 7
    joiningCondition = multiple_15 and unit_100
    if joiningCondition :
        print(i)
        cnt += 1
        if cnt == 3 : break
    i += 1