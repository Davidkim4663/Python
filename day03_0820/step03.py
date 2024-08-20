# 연산자
"""
 연산자 종류
 # 연산자 1개당 자료값 1개
 [1] 산술연산자 +,-,.*,**,/,//,%
 [2] 연결연산자 +," , "
 [3] 비교연산자 >,>=, <, <=, !=, ==
 [4] 논리연산자 >,>=, <, <=, !=, ==
     and = T && T = T.
     or = T || T
     
 [5] 대입연산자 ( = )
     오른쪽 값을 왼쪽 변수에 대입
     +=, -=, *=ㅡ /= , //=, %=

 [6] 삼항연산자 
  
"""
from linecache import clearcache

# 산술연산자 , 반환 리터럴 : 정수 or 실수형
print(10 + 3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 ** 3)  # 1000
print(10 / 3)  # 3.3333333333333335
print(10 // 3)  # 3
print(10 % 3)  # 1

# 연결, 반환 리터럴 : 문자열 1개
print("heufd", "erdeff" + str(3))  # 오류 발생

# 비교, 반환 리터럴 : 불리언 1개
print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)
print(10 == 3)
print(10 != 3)

# 논리 and, or
print(10 > 3 and 20 > 15)  # T and T
print(10 > 3 and 20 > 30)  # T and F = F
print(10 > 3 or 20 > 15)  # T or F = T
print(10 > 3 or 20 > 30)  # T or F = T
print(not (10 > 3))  # F or F = F

# 대입
var1 = 10  # 10 리터럴값을 var1 변수에 대입
print(var1)

var1 = var1 + 10
print(var1)

var1 += 10
print(var1)

var1 -= 10
print(var1)

var1 *= 10
print(var1)

var1 **= 1
print(var1)

var1 /= 2
print(var1)

var1 //= 2
print(var1)

var1 %= 3
print(var1)

# 삼항
import random
point = random.randint(80, 100)
print("point = " + str(point))
# 만약 포인트가 90이상이면 합격이고 아니면 불합격
print("합격") if point >= 90 else print("불합격")

if point >= 90:
    print("합격")
else:
    print("불합격")

# 만약 포인트가 90이상이면 합격이고 아니면 불합격
# [print("최우수")] if point >= 90 else print("꽝")[print("우수")] if point >= 80 else print("꽝")

# [실습] : 기본급과 수당금액을 정수로 입력 받아 실수령액을 계산(기본급 + 수당 - 세금(기본급 10%)
salay = int(input("기본급을 입력하세요 >> "))
salay_수당 = int(input("수당금액을 입력하세요 >> "))

basic_salary = salay
sudang = salay_수당

tax = basic_salary * 0.1

total = (basic_salary + sudang) - tax
print("total = " + str(total))

# 과제_ 연산자