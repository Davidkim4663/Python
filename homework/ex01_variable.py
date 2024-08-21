# [문제1] 변수의 정의
# 변수란 값을 저장하는 공간이며 단 하나의 값 밖에 저장 할 수 없다.

# [문제2] 변수의 선언 (34 , 92.4 , "원숭이" , False)
myAge = 34 # int
myWeight = 92.4 # float
myAnimal = "원숭이" # String
dietIsTomorrow = True # or not(False)

# [문제3] 변수의 변경 age 10
myAge = 10
print("myAge(before) = ", myAge)

myAge = 27
print("myAge(after) = ", myAge) # 변수는 단 하나의 값만 저장 할 수 있으며, 다른 값으로 저장 할 시 기존의 값은 소멸

# [문제4] 변수의 값 호출
"""
name = "유재석"
height = 182.5
gender = True

"""
myName = "김민성"
myHeight = 182.5
myGender = "Male"
myGender = "feMale"

print("myName = ", myName)
print("myHeight = ", myHeight)
if myGender == "Male" : print("myGender = ", myGender)
elif myGender == "feMale" : print(False)

# [문제5] 생각해보기
"""
 [지문] 아래 코드에서 1.변수명, 2.대입연산자, 3.리터럴 값을 찾아 작성하시오.
 phone = "010-3333-3333"
 변수 이름 : Phone
 대입 연산자 : = 
 리터럴 값 : "010-3333-3333"
 
"""

# [문제6] 생각해보기2
"""
[지문] 아래 코드에서 할당된 총 메모리공간의 개수 와 리터럴값 개수를 파악하여 작성하시오. 
coinBox = 3      ==> 메모리 개수 1, 리터럴 값 1 int(4byte)
boolBox = True   ==> 메모리 개수 1, 리터럴 값 1 boolean(2byte)
"""