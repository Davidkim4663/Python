'''
    [문제] 아래 조건을 만족하는 식을 작성하시오.
        [조건1] 사원 번호가 1~30까지 있다.
        [조건2] 남직원은 홀수 번호이고,
        [조건3] 여직원은 짝수 번호이다.
        각각의 번호를 출력하면서 알아볼 수 있게 각 성별을 같이 출력하시오.
    [정답]
        1 남
        2 여
        3 남
        4 여
        ....
'''
i = 1
while i <= 30 :
    employee_Male = i % 2 != 0
    employee_Female = not employee_Male
    
    if employee_Male : print(str(i) + " 남")
    elif employee_Female : print(str(i) + " 여")
    i += 1