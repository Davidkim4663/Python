# [문제1] 튜플의 기본 조작
# [지문]  튜플 (10, 20, 30, 40, 50)이 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.
# [조건]
# 1. 튜플의 첫 번째 원소를 출력하세요.
tuple_ex1 = (10, 20, 30, 40, 50)
print("tuple_ex1 = ", tuple_ex1)
firstIndex_tuple = tuple_ex1[0]
print("튜플의 첫 번째 원소 = ", firstIndex_tuple)

print()
# 2. 튜플의 마지막 원소를 출력하세요.
print("tuple_ex1 = ", tuple_ex1)
lastIndex_tuple = tuple_ex1[len(tuple_ex1) - 1]
print("튜플의 마지막 원소 = ", lastIndex_tuple)

# 3. 튜플의 길이를 출력하세요.
print("tuple_ex1 = ", tuple_ex1)
distance_tuple = len(tuple_ex1) - 1
print("튜플의 길이 = ", distance_tuple)

print()
# [문제2] 튜플의 메소드 사용
# [지문]  튜플 ('apple', 'banana', 'cherry', 'date', 'elderberry')가 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.
tuple_ex2 = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print("tuple_ex2 = ", tuple_ex2)
# [조건]
# 1. 튜플의 두 번째부터 네 번째 원소를 포함하는 새로운 튜플을 생성하여 출력하세요.
tuple_ex2_1 = (tuple_ex2[1: 4])
print("tuple_ex2_1 = ", tuple_ex2_1)

# 2. 튜플의 끝에서 두 번째부터 끝까지의 원소를 포함하는 새로운 튜플을 생성하여 출력하세요.
tuple_ex2_2 = (tuple_ex2[2:])
print("tuple_ex2_2 = ", tuple_ex2_2)
# [문제3] 튜플의 메소드 사용
# [지문]  튜플 (4, 2, 5, 2, 9, 2, 10)이 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.

# [조건]
tuple_ex3 = (4, 2, 5, 2, 9, 2, 10)
print("tuple_ex3 = ", tuple_ex3)
# 1. 튜플에서 숫자 2의 발생 횟수를 출력하세요.
cnt = 0
for i in range(len(tuple_ex3) - 1):
    sameNumber = tuple_ex3[i] == 2
    if sameNumber:
        cnt += 1
print("cnt = ", cnt)
print()
# 2. 튜플에서 숫자 5가 처음 나타나는 인덱스를 출력하세요.
print("tuple_ex3 = ", tuple_ex3)
cnt = 0
findIndex = 0
for i in range(len(tuple_ex3) - 1):
    sameNumber = tuple_ex3[i] == 5
    if sameNumber:
        findIndex = i
        cnt += 1
print("findIndex = ", findIndex)

# [문제4] 튜플의 합치기와 반복
# [지문]  두 개의 튜플 (1, 2, 3)과 (4, 5, 6)이 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.

tuple_ex3_1 = (1, 2, 3)
tuple_ex3_2 = (4, 5, 6)
print("tuple_ex3_1 = ", tuple_ex3_1)
print("tuple_ex3_2 = ", tuple_ex3_2)

# [조건]
# 1. 두 튜플을 합쳐서 새로운 튜플을 생성하여 출력하세요.
tuple_plus = tuple_ex3_1 + tuple_ex3_2
print("tuple_plus = ", tuple_plus)
# 2. 튜플 (7, 8)을 3번 반복한 튜플을 생성하여 출력하세요.
# tuple_ex3_3 = (7, 8)
# tuple_plus_triple = ()
# #  문제 뜻을 이해 못했어요~ 3번 반복해서 append() 하라는 건가요~?
#
# print("tuple_plus_triple = ", tuple_plus_triple)

# [문제5] 튜플의 중첩
# [지문]  튜플 ((1, 2), (3, 4), (5, 6))이 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.
#
# [조건]
tuple_ex5 = ((1, 2), (3, 4), (5, 6))
# 1. 두 번째 내부 튜플의 첫 번째 원소를 출력하세요.
tuple_ex5_first = tuple_ex5[0]
print("tuple_ex5_first = ", tuple_ex5_first)
# 2. 첫 번째 내부 튜플의 두 번째 원소를 변경하여 새로운 튜플을 생성하고 출력하세요

# (튜플의 불변성 때문에 실제로 변경할 수는 없지만 새로운 튜플을 만들어야 합니다).
tuple_ex5[1] = (6, 1)
print("tuple_ex5_second = ", tuple_ex5)

# [문제6] 튜플의 반복문
# [지문]  튜플 ((10, 20), (30, 44), (50, 60))이 주어질 때, 다음을 수행하는 파이썬 코드를 작성하세요.
# [조건]
# 1. 반복문 이용하여 튜플의 모든 요소들의 총합계를 구하시오.
tuple_ex6 = (
    (10, 20),
    (30, 44),
    (50, 60)
)
print("tuple_ex6 = ", tuple_ex6)
total = 0
for i in range(len(tuple_ex6)):
    for j in range(len(tuple_ex6) - 1):
        print(f"tuple_ex6 = {tuple_ex6[i][j]}")
        total += tuple_ex6[i][j]
print("total = ", total)
