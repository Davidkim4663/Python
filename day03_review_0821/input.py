# input() - input의 기본타입은 str
# 주의 ! 입력 시 최초에 선언한 데이터의 타입에 맞게 입력을 받아야, 해당 타입에 맞게 값이 변환된다.
# input()
myName = input("이름을 입력하세요 = ")
print("myName = " + myName)

# int(input())
myAge = input("나이를 입력하세요 = ")
print("myAge = " + myAge)

# float(input())
myWeight = input("몸무게를 입력하세요 = ")
print("myWeight = " + myWeight)

# bool(input())
attendingCLassForTomorrow = input("내일 수업에 참여할거니? yer or no\n")
if attendingCLassForTomorrow == "yes" : print("어서와")
else: print("다음 수업에 와 >< ")
    