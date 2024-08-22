'''
    [문제] 다음 조건이 전부 맞는 수를 출력하시오.
        [조건1] 13의 배수를 전부 검사한다.
        [조건2] 그중 6번째 배수에서 4번째 배수를 뺀 수를 구한다.
        4번째는 배수는 52, 6번째 배수는 78이다.
    [정답]
        26
'''
i = 1
cnt = 0
cnt_4 = 0
cnt_6 = 0
multiple_4 = 0
multiple_6 = 0
while True:
    checkingMultiple = i % 13 == 0
    if checkingMultiple:
        cnt += 1
        if cnt == 4:
            multiple_4 = i
            cnt_4 = cnt
        if cnt == 6:
            multiple_6 = i
            cnt_6 = cnt
            break
    i += 1
print()
print("13 배수 중 6번째 배수 = ", multiple_6)
print("13 배수 중 4번째 배수 = ", multiple_4)

minus = multiple_6 - multiple_4
print("rs = ", minus)
