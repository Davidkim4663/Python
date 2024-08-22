"""
● 함수
 - 함수는 특정한 일을 수행하는 코드의 집합이다.
   이러한 함수를 한 곳에 잘 만들어 놓으면 유지보수, 재사용에 용이하며 가독성을 높일 수 있다.
   또한 함수는 객체 데잍이므로 heap 메모리의 주소값을 참조하고 있다.
   
  - 매개변수, 리턴값

[종류]
 - 입력함수 >> input()
 - 출력함수  >> print()
 - 타입변환 함수 >> int(), float(), str(), bool()
 - 타입확인 함수 >> type()

"""
x = 10
y = 3
z = 1
print(f'1.산술연산자 : {x+y}, {x-y}, {x*y}, {x**y}, {x/y}, {x//y}, {x%y}')
print(f'2.비교연산자 : {x>y}, {x>=y}, {x<y}, {x<=y}, {x==y}, {x!=y}')
print(f'3.논리연산자 : {not(x>=y and y <= z)},{x==y and y == z},{x!=y or y <= z},{x!=y or y <= z}')
x += 2
print(x)
x %= 7
print(x)

# 산술연산자 ex1) 키보드로부터 금액을 입력 받아 금액의 지폐수를 세기

# myMoney = int(input("금액을 입력하세요 "))
# # 만원
# unit_100000 =  myMoney // 100000
# unit_10000 =  (myMoney % 100000) // 10000
# unit_1000 = (myMoney % 10000) // 1000
# unit_500 = (myMoney % 1000) // 500
# unit_100 =(myMoney % 500) // 100
# unit_10 = myMoney % 10
#
# print(f'십만원권 = {unit_100000}\n일만원권 = {unit_10000}\n일천원권 = {unit_1000}\n오백원 = {unit_500}\n백원 = {unit_100}\n십원 = {unit_10}')

# 비교연산자 ex) 국어, 영어, 수학
scoreKor = int(input("국어 점수를 입력하세요 >> "))
scoreEng = int(input("영어 점수를 입력하세요 >> "))
scoreMath = int(input("수학 점수를 입력하세요 >> "))

sum = scoreKor + scoreMath + scoreEng
print("sum", sum)

avg = sum // 3
print("avg",avg)

cutLine = avg >= 90 and scoreKor >= 95 
if cutLine : 
    print("국어우수")
else :
    print("국어장려")






















