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