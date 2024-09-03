# [1] 생성자 : 객체를 생기게 하는 메소드


# 1. 클래스 정의/만들기
class User:
    # 생성자 : 객체를 생성 할 때 메소드 정의
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self( 본인 ) - 해당 메소드를 실행하는 객체 뜻


# 2. 클래스 기반으로 객체 만들기 
u = User('david', 27)
User('minju', 24)

# 3. 객체와 변수의 관계 - 일반적으로 객체는 생성 후 변수에 대입(heap memory)
User('신동엽', 30)  # 아무것도 안할 시 객체를 생성하고 사라진다.

u1 = User('서장훈', 40)  # 객체를 생성하고 객체위치를 변수에 저장한다.
print(u1)

# 4. 객체 주소를 가지고 있는 변수를 통해 객체를 참조 할 수 있다.
# 5. .(도트 연산자 / 접근)
userName = u.name
userAge = u.age
print(userName, "", userAge)

print(u1.name)
print(u1.age)


# [2] 친구 집에 냉장고를 확인하고 싶다.그러면 친구 집의 주소를 알아야 한다.
# 1. 아파트 설계도 / 도면
class Apart:
    def __init__(self, fridge):
        self.fridge = fridge


# 2. 아파트 객체 생성
유재석집 = Apart('바나나')  # 객체 생성과 동시에 냉장고에 '바나나' 대입했다.
강호동집 = Apart('아이스크림')  # 객체 생성과 동시에 냉장고에 '아이스크림' 대입했다.
print(유재석집)
print(강호동집)

refrigerator_유재석 = 유재석집.fridge
print(refrigerator_유재석)

refrigerator_강호동 = 강호동집.fridge
print(refrigerator_강호동)


# ex1) 자동차들을 관리하는 메모리 설계
# 자동차의 고유특성/성질 : 차량번호, 제조자, 현재속도, 
# 문제 : 조건에 따른 고유의 특성을 가지는 클래스를 정의하여 2개의 객체를 생성하고 
#  각 객체 출력

class Car:
    def __init__(self, carNum, carBrand, curCondition):
        self.carNum = carNum
        self.carBrand = carBrand
        self.curCondition = curCondition

    def System(self):
        print(f'현재 이 차에 고유번호는 = {self.carNumber}\n brand = {self.carBrand}\n carCondition = {self.curCondition}.')


car_System = Car('32다 4743', 'HyunDai', '현재 속도 : 100km\n연료량 = 485.32g\n엔진오일 = fine"')

carNumber = car_System.carNum
print("차량번호 = ", carNumber)
car_Brand = car_System.carBrand
print("브랜드 = ", car_Brand)
car_condition = car_System.curCondition
print("상태 = ", car_condition)

print(f'현재 이 차에 고유번호는 = {carNumber}\n brand = {car_Brand}\n carCondition = {car_condition}.')
