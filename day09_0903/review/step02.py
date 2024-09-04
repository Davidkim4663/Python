# [1] 생성자 : 객체를 생기게 하는 메소드
# 1. 클래스 정의 만들기
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self - 해당 메소드를 실행하는 객체 뜻


# 2. 클래스 기반으로 객체 만들기
user1 = User('david', 27)
user2 = User('jenny', 21)
user3 = User('alex', 23)

# 3. 객체주소를 가지고 있는 변수를 통해 객체를 참조 할 수 있다.
userName1 = user1.name
userAge1 = user1.age
print("userName1 = ", userName1, '\nuserAge1 = ', userAge1)

userName2 = user2.name
userAge2 = user2.age
print("userName2 = ", userName2, '\nuserAge2 = ', userAge2)

userName3 = user3.name
userAge3 = user3.age
print("userName3 = ", userName3, '\nuserAge3 = ', userAge3)
print()
print()
# ex) Car
import random

fuel = random.randint(50, 100)
Oil = random.randint(50, 100)
speed = random.randint(100, 200)


class Car:
    def __init__(self, vehicle_number, vehicle_model, fuel_condition, oil_condition, vehice_speed):
        self.vehicle_number = vehicle_number
        self.vehicle_model = vehicle_model
        self.fuel_condition = fuel_condition
        self.oil_condition = oil_condition
        self.vehice_speed = vehice_speed


System = Car("57라 3843", "Avante 5", fuel, Oil, speed)
System_number = System.vehicle_number
System_model = System.vehicle_model
System_Fuel = System.fuel_condition
System_Oil= System.oil_condition
System_speed= System.vehice_speed

print(">>> [myCar System] <<< ")
print(f"차량번호 = {System_number}\n차량모델 = {System_model}")
print("[Car condition]")
print(f"System_Fuel = {System_Fuel}\nSystem_Oil = {System_Oil}\nSystem_speed = {System_speed}")
