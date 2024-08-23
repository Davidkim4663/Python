"""
# 조건문
 어떠한 일의 상태[조건]의 표현 방법 [문:문법]

"""
# 1
c = 'sweet'
d = 'bitter'
if c:
    print("삼킨다")
else:
    print("뱉는다")
import random

# 2
money = random.randint(20000, 100000)  # 네기 가지고 있는 돈
# (1) 만약에 돈이 2만원 이상이면, if 조건문 :
if money >= 20000:
    # 주의할 점 : 들여쓰기
    print("택시를 타고 간다.")
# (2) 만약에 돈이 5만원 이상이면
if money >= 50000:
# 들여쓰기 [키보드에서 Tab 키]
 print('옷 구매')  # True
else:  # 아니면 (5만원 이상이 아니라는 뜻)
 print('아이 쇼핑 한다.')  # False

# (3) 만액에 돈(변수)이 2만원 이상이면
if money >= 20000:
    print('택시를 타고 간다.')
elif money >= 1000:
    print('지하철 타고 간다')
elif money >= 5000:
    print('버스를 타고 간다.')
else:
    print('걸어간다')

    # ex1
score1 = int(input("점수를 입력하세요 >> "))
passScore = score1 >= 80
if passScore:
    print("합격")
else:
    print("불합격")

    # ex2
score2_Str = " "
score2 = int(input("점수를 입력하세요 >> "))
passScore_A = score2 >= 90
passScore_B = score2 < 90 and score2 >= 80
passScore_C = score2 < 80 and score2 >= 70
if passScore_A:
    score2_Str = "A학점"
elif passScore_B:
    score2_Str = "B학점"
elif passScore_C:
    score2_Str = "C학점"
else:
    score2_Str = "재시험"
print(score2, " ", score2_Str)

# ex3 3개의 정수를 입력받아서 오름차순으로 출력하시오
i = 1
while i <= 3:
    firstNum = int(input("정수1를 입력하세요 >> "))
    secondNum = int(input("정수2를 입력하세요 >> "))
    thirdNum = int(input("정수3를 입력하세요 >> "))
    print(firstNum, " ", secondNum, " ", thirdNum)
    i += 1
