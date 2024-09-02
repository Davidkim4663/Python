# [문제1]  리스트 생성과 접근
# [지문] 다음과 같은 리스트 fruits가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
from tkinter.font import names

fruits = ["apple", "banana", "cherry", "date"]
print("fruits = ", fruits)
# [ 출력 조건 예시]
# 1. fruits 리스트의 첫 번째 요소를 출력하세요.
# print(f"첫번째 요소는 = ", fruits[0],f"이며 index = {fruits.count("apple")}" )

# 2. fruits 리스트의 마지막 요소를 출력하세요.
# lastIndex_Fruits = fruits[len(fruits) - 1]
# print("lastIndex_Fruits = ", lastIndex_Fruits)

# 3. fruits 리스트에서 "banana"의 인덱스를 찾으세요.
# findIndex = fruits.index("banana")
# print(f"첫번째 요소는 = ", fruits[1],f"이며 index = {fruits.count("banana")}" )

# [문제2]  리스트 수정
# [지문] 다음과 같은 리스트 numbers가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
numbers = [10, 20, 30, 40, 50]
print("numbers = ", numbers)

# [ 출력 조건 예시]
# 1. numbers 리스트의 두 번째 요소를 25로 변경하세요.
print()
# print("변경 전 = ", numbers)
# print("변경 전 = ", numbers)
# secondIndex = numbers.index(20)
# numbers[secondIndex] = 25
# print("변경 후 = ", numbers)

# 2. numbers 리스트에 60을 추가하세요.
# print()
# print("변경 전 = ", numbers)
# numbers.append(60)
# print("변경 후 = ", numbers)
# # 3. numbers 리스트에서 마지막 요소를 제거하세요.
# print()
# print("변경 전 = ", numbers)
# lastIndex_n = numbers[len(numbers) - 1]
# removeIndex_r = numbers.remove(lastIndex_n)
# print("변경 후 = ", numbers)

# [문제3]  리스트 슬라이싱 과 연결
# [지문] 다음과 같은 리스트 list1과 list2가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("list1 = ", list1)
print("list2 = ", list2)
# [ 출력 조건 예시]
# 1. list1의 첫 번째부터 세 번째 요소까지 슬라이싱하여 출력하세요.
# list1_1_to_3 = list1[0 : 3]
# print("list1_1_to_3 = ", list1_1_to_3)

# 2. list1 과 list2의 모든 요소를 포함하는 리스트 list3를 생성하여 출력하세요.
# 리스트 연결
list3 = []
list1.extend(list2)
list3.append(list1)
# .extend()를 사용하면 list3 리스트 안에 list1,list2가 합쳐진 리스트가 들어간다 [[]]
# listConnect = list1 + list2
# print("listConnect() : ",listConnect)
# list3.append(listConnect)
print("list3 : ",list3)


# [문제4]  리스트 내포
# [지문] 다음과 같은 리스트 values가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
values = [1, 2, 3, 4, 5]
print("values = ", values)
# [ 출력 조건 예시]
# 1. values의 각 요소를 제곱한 새로운 리스트 squared_values를 만드세요.
squared_values = []
for i in range(len(values)) :
    double_number = values[i] * 2
    squared_values.append(double_number)
print("squared_values = ", squared_values)
# 2. values에서 짝수만 포함하는 리스트 even_values를 만드세요.
print("values = ", values)
print()
even_values = []
for i in range(len(values)) :
    even_number_check = values[i] % 2 == 0
    if even_number_check :
        even_values.append(values[i])
print("even = ", even_values)
# [문제5]  중첩 리스트
# [지문] 다음과 같은 리스트 matrix가 있습니다 아래 출력 조건에 따라 코드를 작성하시오,
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("matrix = ", matrix)
print()
# [ 출력 조건 예시]
# 1. matrix의 첫 번째 행을 출력하세요.
print("첫번째 행 = ", matrix[0])
# 2. matrix의 두 번째 열을 출력하세요.
print("첫번째 행 = ", matrix[2])
# 3. matrix의 중앙 요소를 출력하세요.
print("첫번째 행 = ", matrix[1])
