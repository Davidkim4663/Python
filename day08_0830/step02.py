# [7] 함수 안에서 선언된 변수의 사용 범위 #지역변수, 전역변수
var1 = int(input(">>"))


def test1():
    global var1
    var1 = var1 + 1


print("dd", var1)


# 1. return 반환 -> 전역변수와 지역변수가 이름이 동일하면 함수 내에서 지역변수가 우선
# why? 지역변수를 사용하는 이유
# > 즉 함수를 사용하는 이유 : 함수를 정의하고 함수 내 코드들은 실행 할 때만 메모리에 할당 후 종료되면 사라짐
def test2(var1):
    var1 = var1 + 1
    return var1
    # 지역변수의 자료를 반환


print(test2(var1))

# 전역
def test3():
    global var1
    var1 = var1 + 2


print(test3())
print(var1)

# [실습1] : 키보드로 부터 입력 받은 2개의 정수를 인자값으로 전달하여 두 정수를 제곱 결과 반환
num1 = int(input("[정수1] \n>>"))
num2 = int(input("[정수2] \n>>"))
def double(num1, num2):
    return calc_num1, calc_num2

calc_num1 = num1 ** num1
calc_num2 = num2 ** num2

doubleNum = double(calc_num1, calc_num2)
print("rs =", doubleNum)

# [실습2]
listNum = [1, 2, 3, 4]
calc = 0
def total(calc) :
    for i in range(len(listNum)) :
        calc += listNum[i]
    return calc
totalScore = total(calc)
print("totalScore = ", totalScore)