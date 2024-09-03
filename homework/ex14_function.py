# [문제1] 문자열 길이 반환
# [ 지문 ]  하나의 문자열을 입력받아 그 문자열의 길이를 반환하는 string_length 함수를 정의하세요.

# [ 요구사항 ]
# 1. string_length 함수는 하나의 문자열을 매개변수로 받아야 합니다.
# 2. 문자열의 길이를 반환하세요.
# 3. 함수 호출 예시: string_length("hello")는 5를 반환해야 합니다.
ex1_str = input("문자열 하나를 입력하세요 >> ")
print("ex1_str = ", ex1_str)
def string_length(ex1_str) :
    return ex1_str

checkingLength = string_length(len(ex1_str))
print(f"입력 받은 문자열의 길이는 {checkingLength} 입니다")

# [문제2] 최대값 찾기
# [ 지문 ]  정수로 이루어진 리스트를 입력받아 그 리스트에서 최대값을 반환하는 find_max 함수를 정의하세요.
# [ 요구사항 ]
# 1. find_max 함수는 정수 리스트를 매개변수로 받아야 합니다.
# 2. 리스트에서 가장 큰 값을 반환하세요.
# 3. 리스트가 비어있으면 0을 반환하세요.
# 4. 함수 호출 예시: find_max([1, 3, 2, 5, 4])는 5를 반환해야 합니다.
import random
numberList = []
for i in range(5) :
    numberbox = random.randint(1, 10)
    numberList.append(numberbox)
print("numberList = ", numberList)
max = 0
def find_max(max) :
    for i in range(len(numberList)) :
        maxCheck = max <= numberList[i]
        if maxCheck :
            max = numberList[i]
        else :
            numberList[i] = 0
    return max
maxNumber = find_max(max)
print("maxNumber = ", maxNumber)


# [문제3] 두 숫자의 차이
# [ 지문 ]  두 개의 정수를 입력받아 그 차이를 반환하는 subtract_numbers 함수를 정의하세요.
# [ 요구사항 ]
# 1. subtract_numbers 함수는 두 개의 정수 매개변수를 받아야 합니다.
# 2. 두 정수의 차이를 반환하세요 (첫 번째 정수에서 두 번째 정수를 뺍니다).
# 3. 함수 호출 예시: subtract_numbers(10, 4)는 6을 반환해야 합니다.
ex3_num1 = int(input("[정수 1] 입력\n>> "))
print("ex_num1 = ", ex3_num1)

ex3_num2 = int(input("[정수 2] 입력\n>> "))
print("ex_num2 = ", ex3_num2)


def subtract_numbers(ex3_num1, ex3_num2):
    return ex3_num1 - ex3_num2

comparsion_num = subtract_numbers(ex3_num1, ex3_num2)
print("두 정수의 차이 = ", comparsion_num)

# [문제4] 문자열 역순
# [ 지문 ] 하나의 문자열을 입력받아 그 문자열을 역순으로 변환하여 반환하는 reverse_string 함수를 정의하세요.
# [ 요구사항 ]
# 1. reverse_string 함수는 하나의 문자열을 매개변수로 받아야 합니다.
# 2. 문자열을 역순으로 변환하여 반환하세요.
# 3. 함수 호출 예시: reverse_string("hello")는 "olleh"를 반환해야 합니다.

ex3_str = input("문자열 하나를 입력하세요 >> ")
print("ex1_str = ", ex3_str)
def string_length(ex3_str) :
    return ex3_str

checkingReverse = string_length(ex3_str[:: -1])
# slice로 뒤집기
print(f"입력 받은 문자열 = {checkingReverse} 입니다")


# [문제5] 숫자 제곱
# [ 지문 ] 하나의 문자열을 입력받아 모든 문자를 대문자로 변환하여 반환하는 to_uppercase 함수를 정의하세요.
# [ 요구사항 ]
# 1. square_number 함수는 하나의 숫자 매개변수를 받아야 합니다.
ex5_int = int(input("숫자 하나를 입력하세요\n >> "))
def square_number (ex5_int) :
    return ex5_int*ex5_int

doubleNum = square_number(ex5_int)
print("숫자 제곱 = ", doubleNum)

# 2. 입력받은 숫자의 제곱을 반환하세요.
# 3. 함수 호출 예시: square_number(4)는 16을 반환해야 합니다.
