# 리스트 [] : 어떤 자료의 값을 일정한 순서로 적은 것

#  리스트의 인덱싱과 슬라이싱
student = ["유재석", "신동엽", "강호동", "서장훈"]
print("studentList = ", student)

# 슬라이싱 : 인덱싱을 이용한 오소들 추출 index - 1
# print(student[0 : 2]) # 0 ~ 1 유재석, 신동엽
# print(student[0 : 3]) # 0 ~ 2 유재석, 신동엽, 강호동
# print(student[  : 1]) # index의 마지막 요소 전까지 슬라이싱 -> 서장훈
# print(student[3 : ]) # index의 마지막 요소 전까지 슬라이싱 -> 서장훈
# print(student[ : ])
# print(student[0 : 4 : 1])
# print(student[-1 : -5 : -1]) # -1부터 -4까지 1씩 증가
# print(student[-1 : -5 : -2]) # -1부터 -4까지 1씩 증가
