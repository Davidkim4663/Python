# [문제1]
# [지문]  하나의 점수를 정수형으로 입력받아 점수가 90점 이상이면 '합격' 아니면 '불합격' 출력 하시오.
# ex1Score = int(input("점수를 입력하세요 >> "))
# passScore = ex1Score >= 90
# failScore = not passScore
# if passScore :
#     print("합격")
# elif failScore :
#     print("불합격")
# # [문제2]
# # [지문]  하나의 점수를 정수형으로 입력받아 점수가 90점 이상이면 'A등급', 80점 이상이면 'B등급', 70점 이상이면 'C등급', 그외 '재시험' 으로 출력 하시오.
# ex2Score = int(input("점수를 입력하세요 >> "))
# grade_A = ex2Score >= 90
# grade_B = ex2Score >= 80
# grade_C = ex2Score >= 70
# grade_fall = not(grade_A and grade_B and grade_C)
# grade_Str =  " "
# if grade_A :
#     grade_Str = "A등급"
# elif grade_B :
#     grade_Str = "B등급"
# elif grade_C :
#     grade_Str = "C등급"
# elif grade_fall :
#     grade_Str = "재시험"
# print(grade_Str)
# [문제3]
# [지문]  각 3개의 정수형으로 수를 입력받아 가장 큰 수를 출력 하시오. [ 전제조건 : 각 정수는 서로 다른 정수값 ]
oneNumber = int(input("[정수1]를 입력 하세요 \n>> "))
anotherNumber =  int(input("[정수2]를 입력 하세요 \n>> "))
otherNumber =  int(input("[정수3]를 입력 하세요 \n>> "))
print(oneNumber," ",anotherNumber," ",otherNumber, end="\n")

oneNumber_Big = (oneNumber > anotherNumber) and (oneNumber > otherNumber)
anotherNumber_Big = (anotherNumber > oneNumber) and ( anotherNumber > otherNumber)
otherNumber_Big = (otherNumber > oneNumber) and ( otherNumber > anotherNumber)

max = 0
if oneNumber_Big :
    max = oneNumber
elif anotherNumber_Big :
    max = anotherNumber
elif otherNumber_Big :
    max = otherNumber
print("max = ", max)

# [문제4]
# [지문]  각 3개의 정수형으로 수를 입력받아 오름차순 순서대로 출력하시오. [ 전제조건 : 각 정수는 서로 다른 정수값 ]
import random

choice = random.randint(0, 1)
choice_oneNumber = int(input("[정수1]를 입력 하세요 \n>> "))
choice_anotherNumber = int(input("[정수2]를 입력 하세요 \n>> "))
choice_otherNumber = int(input("[정수3]를 입력 하세요 \n>> "))




