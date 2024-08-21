'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.
        [조건1] 사원 번호가 1~30까지 있다.
        [조건2] 1~5번은 과장
        [조건3] 6번에서 15는 대리
        [조건4] 16번에서 30번은 사원이다.
        각각의 번호를 출력하면서 알아볼 수 있게 각 명칭을 같이 출력하시오.
    [정답]
        1 과장
        2 과장
        ...
        ...
        ...
        6 대리
        ...
        ...
        ...
        16 사원
        ...
        ...
        ...
'''
i = 1
while i <= 30 :
    exaggeration = i >= 1 and i <= 5
    agent = i >= 6 and i <= 15
    staff = i >= 16 and i <= 30
    if exaggeration : print(str(i) + " = 과장")
    elif agent : print(str(i) + " = 대리")
    elif staff : print(str(i) + " = 사원")
    i += 1