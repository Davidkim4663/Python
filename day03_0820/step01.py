# day 03
# 주석 : 실행 X , 설명 or 메모
10  # 자료, 정수타입

# type(자료)
type(10.5)  # 자료의 타입변환 / 알려주는 함수

# int(),float(),str(),bool(자료) # 문자열 자료를 각 타입으로 변환해주는 내장함수
# int('10')
# float('10.5')
# float('True')

# 변수의 선언하고 초기화, 변수명 = 초기값
# var = 10
#
# # 변수의 자료 / 값 호출
# # var
#
# # 변수의 자료 / 값 수정 , 변수명  = 새로운 값
# var = 5

# 콘솔창에 출력함수, print(자료 / 변수명)
# print(var)
# print(f'var : {var}')  # 문자열과 변수의 값을 같이 출력 할 수 있다.
# print(f'var : \t {var} \n')  # 문자열과 변수의 값을 같이 출력 할 수 있다 + \n \t .

# 입력함수
# 콘솔에서 입력 후 엔터 기준으로 입력값을 <class 'str'>반환함수
# 콘솔창에 초록색 부분이 
# 입력된 값, 검정색 부분이 출력된 값
input()
# 하나의 데이터를 입력 받아서 출력하시오
print(type(input()))  # <class 'str'>
# 하나의 정수 데이터를 입력 받아서 출력 하시오
# print(type(int(input()))) int()를 씌우면 타입이 str에서 int로 변환
print(int(input()))

# 하나의 정수 데이터를 입력 받아서 변수에 저장하고 변수를 출력하시오
int(input())
# 변수 저장
num = int(input())

# 변수값 호출
print("var =  " + str(num))





















