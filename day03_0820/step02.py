# day03
# 실습1


# 주의할점
"""
 입력 시 정해진 데이터 타입으로만 입력을 해야 값을 전달할 수 있다.
 입력 시 정해진 데이터가 아닌 다른 타입으로 입력 시 전달이 안된다.
 
 타입과 형식
 type

"""
name = input("이름을 입력하세요 >> ")      # 이름 str

age = int(input("나이를 입력하세요 >> "))  # 나이 int

weight = float(input("몸무게를 입력 >> ")) # 몸무게 float

mzOrnot = bool(input("당신은 mz 입니까 >>")) # mz bool

myName = name
myAge = age
myWeight = weight
myMZ = mzOrnot


print("myName : " + myName)
print("myAge : " + str(myAge))
print("myWeight : " + str(weight))
if myMZ == "True" or "False" : print("myMZ : " + str(myMZ))

