"""
    파이썬에서 데이터를 다루는 방법 / 문법
    - 정수, 실수, 문자열, 불리언
    - 리스트[], 튜플(), 딕셔너리 {}
"""

# [1] 자료가 4개를 하나의 자료로 표현 ex : "유재석"(문자열 1개), 41(정수1개), 193,1(실수 1개), False(불리언 1개)
# [2] 변수와 자료의 관계 : 변수는 자료 1개를 저장하는 메모리 공간 (저장개념)
expression_List = ["유재석", 41, 193.1, False]
expression_tuple = ("유재석", 41, 193.1, False)
expression_dic = {"name": "유재석", "age": 41, "height ": 182.1}
print()
print("expression_List = ", expression_List)
print("expression_tuple = ", expression_tuple)
print("expression_dic = ", expression_dic)
print()

# [3] 변수를 이용한 리스트/튜플/딕셔너리를 추가, 수정, 삭제, 호출(CRUD)
# 1. 리스트 요소 추가
expression_List.append("인천시")
print("expression_List(추가) = ", expression_List)

# 1-1 리스트 호출
# print(list[x])

# 2. 튜플 (값 변경 불가능)
# expression_tuple.
# 2-2 튜플 호출
# print(tuple[0])

# * 리스트와 튜플은 인덱싱을 이용하고, 딕셔너리는 키를 이용해서 값을 불러온다.

# 3. 딕셔너리
expression_dic['addr'] = "인천시"
print("expression_dic(추가) = ", expression_dic['addr'])

expression_List[0] = "강호동"
print("expression_List(수정) = ", expression_List)

# expression_tuple[0] = "강호동"
# print("expression_tuple(수정) = ",expression_tuple)
print("expression_tuple(수정) -> 튜플은 불변성으로 인해 수정이 불가능하다.")
expression_dic['name'] = "강호동"
print("expression_dic(수정) = ", expression_dic)
print()
# 삭제 * 튜플은 삭제도 불가능
expression_List.remove("인천시")
print("expression_List(삭제) = ", expression_List)

del expression_dic['addr']
print("expression_dic(삭제) = ", expression_dic)

"""
 함수란 ?
  어떤 코드의 집합 
  매개변수들의 값을 처리하고 결과를 리턴한다.
"""


# [1] 함수 만들기 정의
def 믹서기(과일):
    print('믹서기 실행 중 (과일쥬스를 만들고 있습니다) ')  # 실행코드
    return f"{과일} 쥬스"  # 함수가 종료 될 때 반환되는 자료


# [2] 힘수 시용/호출 #함수명() 함수에 전달할 인자값
# 함수를 호출해서
쥬스컵 = 믹서기('바나나')
print(쥬스컵)


# 매개변수와 리턴/반환
# 1. 매개변수 O, 리턴값 O 함수
def add(a, b):  # 함수 명령어
    return a + b


# 2. 함수 호출 사용
sum = add(5, 7)
print(sum)


# 3. 매개변수 X, return O
def say():
    return 'hi'


hi = say()
print(hi)


# 4. 매개변수, 리턴값 x
def say2():
    print('hi')


say2()


# 5. 매개변수 O, 리턴값 x
def add2(a, b):
    print(a + b)


#  매개변수가 없거나 ,리턴값이 없을 경우에는 함수 호출 시 반환되는 값이 없으므로 NONE
add2(b=1, a=5)


# 6. 매개변수의 개수가 n개일 때
def add_many(*param):
    print(param)

add_many(1, 2, 3, 4, 5, 6)
add_many(1, 2, 3)

# 가변길이 매개변수를 사용할 때는 특정 매개변수와 가변길이 매개변수를
# 같이 사용 할 시 가변길이매개변수는 맨 뒤에 사용해야한다
# ex)
# def add_mul(*param, choice) :
def add_mul(choice, *param) :
    print(choice)
    print(param)

add_mul('h1', 1,2,3)
add_mul('h1', 1,2,3)