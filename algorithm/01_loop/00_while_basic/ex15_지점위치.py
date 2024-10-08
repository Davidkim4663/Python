'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.
        [조건1] 편의점 지점번호가 1~30까지 있다.
        [조건2] 5번 이하의 지점의 위치는 서울이다.
        [조건3] 25번 이상의 지점의 위치는 서울이다.
        [조건4] 위 지점을 제외한 다른 모든 지점의 위치는 경기이다.
        각각의 번호를 출력하면서 알아볼 수 있게 각 지점 위치를 같이 출력하시오.
    [정답]
        1 서울
        2 서울
        ...
        6 경기
        ...
        25 서울
        ...
'''
i = 1
while i <= 30 :
    branch_Seoul = i <= 5 or i >= 25
    branch_Gyeonggi = not branch_Seoul
    if branch_Seoul : print(str(i) + " 서울")
    elif branch_Gyeonggi : print(str(i) + " 경기")
    i += 1