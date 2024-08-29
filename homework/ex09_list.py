# [문제1]  리스트 요소 출력
# [지문] 다음과 같은 리스트 colors가 있습니다. 아래 출력 조건에 따라 코드를 작성하시오,
from html.entities import entitydefs

colors = ["red", "blue", "green", "yellow"]
# [ 출력 조건 예시]
# 1. colors 리스트의 모든 요소를 한 줄씩 출력하세요. (반복문을 사용하세요.)
for i in range(len(colors)) :
    print(colors[i], end=" ")

# [문제2]  리스트의 합과 평균
# [지문] 다음과 같은 리스트 numbers가 있습니다. 아래 출력 조건에 따라 코드를 작성하시오,
#
print("\n")
numbers = [5, 10, 15, 20, 25]
print("numbers = ", numbers)
# [ 출력 조건 예시]
# 1. numbers 리스트의 모든 요소의 합을 계산하여 출력하세요.
total = 0
for i in range(len(numbers)) :
    total += numbers[i]
print("total = ", total)

# 2. numbers 리스트의 요소의 평균을 계산하여 출력하세요. (반복문을 사용하세요.)
sum = total
avg = 0
for i in range(len(numbers)) :
    avg = sum // len(numbers)
print("avg = ", avg)


# [문제3] 리스트 내 요소 2배로 만들기
# [지문] 다음과 같은 리스트 values가 있습니다. 아래 출력 조건에 따라 코드를 작성하시오,
#
values = [1, 2, 3, 4, 5]
# [ 출력 조건 예시]
# 1. values 리스트의 모든 요소를 2배로 만든 새로운 리스트 doubled_values를 생성하여 출력하세요. (반복문을 사용하세요.)
doubled_values = []
calc = 0
for i in range(len(values)):
    calc = values[i] * 2
    doubled_values.append(calc)
print("doubled_values = ", doubled_values)

# [문제4]  짝수 필터링
# [지문] 다음과 같은 리스트 mixed_numbers가 있습니다. 아래 출력 조건에 따라 코드를 작성하시오,

mixed_numbers = [12, 7, 34, 19, 23, 8]
print("mixed_numbers = ", mixed_numbers)
# [ 출력 조건 예시]
# 1. mixed_numbers 리스트에서 짝수만 포함하는 새로운 리스트 even_numbers를 생성하여 출력하세요. (반복문을 사용하세요.)
even_numbers = []
even = 0
for i in range(len(mixed_numbers)):
    even = mixed_numbers[i] % 2 == 0
    if even :
        even_numbers.append(mixed_numbers[i])
print("even_numbers = ", even_numbers)


# [문제5]  리스트의 중복 제거
# [지문] 다음과 같은 리스트 duplicates가 있습니다. 아래 출력 조건에 따라 코드를 작성하시오,
#
print()
duplicates = [1, 2, 2, 3, 4, 4, 5]
print("변경 전 = ", duplicates)
changeDup = [] # 중복 제거된 값들이 들어갈 리스트

for value in duplicates:
    if value not in changeDup: # 중복제거
        changeDup.append(value)

print("변경 후 = ", changeDup)
