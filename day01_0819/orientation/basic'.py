print(1 + 1)
print("hello world")
'''
 파이썬 (프로그래밍 언어) : 소통을 하기 위해 만들어진 규칙과 기호집합
 데이터 자료 : 정수, 실수, 문자열, 리스트, 튜플, 딕셔너리, 불리언, 등등 형태로 된 의미단위
 1. 정수(Integer) : 정수는 소수점이 없는 숫자
 2. 실수(Float) : 정수는 소수점이 있는 숫자
 3. 문자열(String) : 문자들의 집합
 4. 리스트 : []
 5. 튜플 : ()
 6. 딕셔너리 : {}
 7. 불리언 : T/F
 
'''

# 주석 : 번역 되지 않는 코드
# Literal : 파이썬에서 미리 정해둔 데이터
# 타입분류 : 정수, 실수, 문자열, 불리언

# 1. 데이터들의 타입확인
print(123) # 자동완성
print("123") # 자동완성

print(type(123))  # int
print(type("123")) # str
print(type(10 < 3)) #boolean
print(type(10.3)) #float
print(type(True)) #boolean

# 2. 기본 타입 종류와 데이터들의 형태
# 2-1 정수 타입
print(3)
print(3232323)
print(3232323 + 3)

# 2-2 실수 타입, 일반적인 소수점 형식의 데이터
print(3.13)
print(12.0 + 13.0)

# 2-3 불리언 타입 , True, false
print(True)
print(False)
print(10>3)

# 2-4 문자열 타입 -> 어떤 타입이든 "",''로 감싸면 문자열이 된다.
print("안녕")
print('안녕')
print('''안녕''')