# OOP(Object Oriented Programming)
"""
 클래스란?
  - 객체를 만들기 위한 설계도/틀
  - 클래스 만들 때는 첫 글자는 대문자(함수인지 클래스인지 구분)
"""
# [1] 클래스 만들기 class(키워드)
class Human :
    pass # pass : 아무것도 수행하지 않는 문법(임시용)

# [2] 객체 만들기
Human()
print(Human())
print(type(Human))

h1 = Human()
h2 = Human()
print(h1)
print(h2)

# [3] 클래스 만들기
class 붕어빵 :
    def __init__(self, 내용물):
        self.내용 = 내용물

# [4] 붕어빵 객체
붕어빵1 =  붕어빵('팥')
붕어빵2 =  붕어빵('크림')
print(붕어빵1)
print(붕어빵2)

# [5] 자동차 클래스 만들기
class Car :
    # 생성자
    def __init__(self, carNumber):
        self.carNumber = carNumber
    # 함수
    def move(self):
        print(f'{self.carNumber}가 전진한다.')
        
    def backward(self):  
        print(f'{self.carNumber}가 후진한다.')
        
    def left(self):
        print(f'{self.carNumber}가 좌회전한다.')

    def right(self):
        print(f'{self.carNumber}가 우회전한다.')

# [6] 자동차 객체
유재석차 = Car('123') # 객체생성
강호동차 = Car('4567') # 객체생성
print(유재석차)
print(강호동차)

유재석차.move()
유재석차.backward()
유재석차.move()
강호동차.backward()

# 딕셔너리 vs 클래스(객체)


