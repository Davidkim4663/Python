# 반복문
"""
 제어문 : 특정 상황에 따라 코드 흐름을 제어한다.
  - IF (조건문)
  - FOR (반복문)
"""

# ex1) [조건문] : 3개의 정수를 입력 받아서 가장 큰 수를 출력 하시오
oneNumber = int(input("[정수1]를 입력 하세요 \n>> "))
anotherNumber =  int(input("[정수2]를 입력 하세요 \n>> "))
theotherNumber =  int(input("[정수3]를 입력 하세요 \n>> "))
print(oneNumber," ",anotherNumber," ",theotherNumber, end="\n")

oneNumber_Big = (oneNumber > anotherNumber) and (oneNumber > theotherNumber)
anotherNumber_Big = (anotherNumber > oneNumber) and ( anotherNumber > theotherNumber)
otherNumber_Big = (theotherNumber > oneNumber) and ( theotherNumber > anotherNumber)

max = 0
if oneNumber_Big :
    max = oneNumber
if anotherNumber_Big :
    max = anotherNumber
if otherNumber_Big :
    max = theotherNumber
print("max = ", max)

# ex2) [조건문] : 3개의 정수를 입력 받아 내림차순으로 출력하시오
firstNum = int(input("[정수1]를 입력 하세요 \n>> "))
secondNum =  int(input("[정수2]를 입력 하세요 \n>> "))
thirdNum  =  int(input("[정수3]를 입력 하세요 \n>> "))

firstNum_Min = (firstNum < secondNum) and (firstNum < thirdNum)
secondNum_Min = (secondNum < firstNum) and ( secondNum < thirdNum)
thirdNum_Min = (thirdNum < firstNum) and ( thirdNum < secondNum)

box = 0

if firstNum_Min :
    box = firstNum # box 10 == firstNum 10
    firstNum = secondNum # firstNum 20 secondNum 20
    secondNum = thirdNum # secondNum 30 = thirdNum = 30
    thirdNum = box
    print(firstNum,secondNum,thirdNum,end=" ")
if secondNum_Min :
    box = secondNum # box 10 == firstNum 10
    secondNum = thirdNum # firstNum 20 secondNum 20
    thirdNum = firstNum # secondNum 30 = thirdNum = 30
    firstNum = box
    print(firstNum,secondNum,thirdNum,end=" ")
if thirdNum_Min :
    box = thirdNum # box 10 == firstNum 10
    firstNum = secondNum # firstNum 20 secondNum 20
    secondNum = thirdNum # secondNum 30 = thirdNum = 30
    thirdNum = box
    print(firstNum,secondNum,thirdNum,end=" ")

#  내림차순 연습하기
