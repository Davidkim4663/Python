# [문제1]  리스트 생성과 접근
# [지문] 다음과 같은 리스트 fruits가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
from day06_0827.step03 import memberList

fruits = ["apple", "banana", "cherry", "date"]
# [ 출력 조건 예시]
# 1. fruits 리스트의 첫 번째 요소를 출력하세요.
firstIndex = fruits[0]
print("firstIndex = ", firstIndex)
# 2. fruits 리스트의 마지막 요소를 출력하세요.
lastIndex = len(fruits) - 1
print("lastIndex = ", fruits[lastIndex])

# 3. fruits 리스트에서 "banana"의 인덱스를 찾으세요
findIndex = fruits.index("banana")
print("index = fruits[", findIndex, "] findIndex = ", fruits[findIndex])

print()
# [문제2]  리스트 수정
# [지문] 다음과 같은 리스트 numbers가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
numbers = [10, 20, 30, 40, 50]
print("변경 전 = ", numbers)
# [ 출력 조건 예시]
# 1. numbers 리스트의 두 번째 요소를 25로 변경하세요.
numbers[1] = 25
print("변경 후 = ", numbers)

# 2. numbers 리스트에 60을 추가하세요.
numbers.append(60)
print("변경 후 >> ", numbers)

# 3. numbers 리스트에서 마지막 요소를 제거하세요.
# numbers.remove(60)
# print("마지막 요소 제거 >> ", numbers)

numbers.pop(5)
print("마지막 요소 제거 >> ", numbers)

# [문제3]  리스트 슬라이싱 과 연결
# [지문] 다음과 같은 리스트 list1과 list2가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("list1 = ", list1)
print("list2 = ", list2)

# connection_list = list1 + list2
# print("리스트 연결 = ", connection_list)

# list1.extend(list2)
# print("extendList = ", list1)

# 1. list1의 첫 번째부터 세 번째 요소까지 슬라이싱하여 출력하세요.
print(list1[3:])

# 2. list1 과 list2의 모든 요소를 포함하는 리스트 list3를 생성하여 출력하세요.
list3 = []
connectionList3 = list1 + list2
list3.append(connectionList3)
print("list3 = ", list3)

# [문제4]  리스트 내포
# [지문] 다음과 같은 리스트 values가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
values = [1, 2, 3, 4, 5]
# [ 출력 조건 예시]
print("values = ", values)
# 1. values의 각 요소를 제곱한 새로운 리스트 squared_values를 만드세요.
squared_values = []
calc = 0
for i in range(len(values)):
    calc = values[i] * 2
    squared_values.append(calc)
print("squared_values = ", squared_values)

print()
# 2. values에서 짝수만 포함하는 리스트 even_values를 만드세요.
print("values = ", values)
even_values = []

for i in range(len(values)):
    even = values[i] % 2 == 0
    if even:
        even_values.append(values[i])

print("짝수 = ", even_values)

# [문제5]  중첩 리스트
# [지문] 다음과 같은 리스트 matrix가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# [ 출력 조건 예시]

# 1. matrix의 첫 번째 행을 출력하세요.
first_row = matrix[0]
print(first_row)

# 2. matrix의 두 번째 열을 출력하세요.
for i in range(len(matrix)):
    second_column = matrix[i][1]
    print(second_column, end=" ")

print()
# 3. matrix의 중앙 요소를 출력하세요.
print(matrix[1][1])
