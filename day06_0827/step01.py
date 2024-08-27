"""
# 리스트 [] : 어떤 자료의 값을 일정한 순서로 적은 것
"""
import random

# [1] 리스트 타입 형태 : 여러 개의 자료들을 쉼표로 구분하고 [] 대괄호 감싼 형식
odd = [1, 3, 4, 5, 7, 9]
print("odd = ", odd)

a = []  # 요소가 없는 리스트 선언 un
print(a)

b = ["life", "is", "too", "short"]
print(b)

c = [1, 2, True, 'Life', 'is']  # 여러가지 타입의 요소들 5개인 리스트 선언

d = (1, 2, ['Life', 'is'])  # 여러가지 타입의 요소들
print(d[2])

# 리스트의 인덱싱과 슬라이싱
student = ['유재석', '신동엽', '강호동', '서장훈']
print("index 0 = ", student[0])
print("index 1 = ", student[1])
print("index 2 = ", student[2])
print("index 3 = ", student[3])
print()
print("index 1 = ", student[-1])
print("index 2 = ", student[-2])
print("index 3 = ", student[-3])
print("index 3 = ", student[-4])
student.append("이승기")
print(student)
student.remove("이승기")
print(student)

# 인덱싱 : 인덱스를 이용한 요소 추출
# 슬라이싱 : 인덱싱을 이용한 요소들 추출

print(student[0 : 2]) # 0 ~ 1
print(student[0 : 3]) # 0 부터 2미만(1까지), 0 ~ 2
print(student[ : 4 ]) # 0 부터 4미만(3까지), 0 ~ 3
print(student[2 : ])  # 생략 시 마지막 인덱스
print(student[ : ]) # 전체 생략시 전체 호출
print(student[0 : 4 : 1]) # 0부터 3까지 1씩 증가
print(student[-1 : -5 : -1]) # -1부터 -4까지 1씩 증가
print(student[-1 : -5 : -2]) # -1부터 -4까지 2씩 증가
