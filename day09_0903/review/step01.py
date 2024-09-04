"""
 OOP(Object Oriented Programming)
 * class
  - 객체를 만들기 위한 설계도 or 틀
  - 클래스를 만들 때는 첫 글자 대문자로 작성하는 것을 권장
"""


# [1] 클래스 만들기 class(키워드)
class Human :
    pass # 아무것도 수행하지 않는 문법(임시용)
# [2] 객체 만들기
Human()
print(Human())
print(type(Human))

h1 = Human()
h2 = Human()
print("h1 = ", h1)
print("h2 = ", h2)

# [3] 클래스 만들기
class 붕어빵 :
    def __init__(self, 내용물):
        self.내용물 = 내용물

# [4] 붕어빵 객체
붕어빵1 = 붕어빵('팥')
붕어빵2 = 붕어빵('크림')
print("붕어빵1 = ", 붕어빵1)
print("붕어빵2 = ", 붕어빵2)

붕어빵1.내용물 = "팥"
붕어빵2.내용물 = "크림"
팥붕 = 붕어빵1.내용물
슈붕 = 붕어빵2.내용물

print("팥붕 = ", 팥붕)
print("슈붕 = ", 슈붕)

# 자동차 클래스
class Car : 
    # 생성자 함수
    def __init__(self, carNumber) :
        self.carNumber = carNumber

    def move(self):
        print(f"내 차량번호 = {self.carNumber}가 움직인다")

myCar = Car("23다 3321")
myCarId = myCar.carNumber
print("myCarID = ", myCarId)
myCar.move()

