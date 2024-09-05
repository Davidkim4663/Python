# 실습 1 : 계산기(다시)

num1 = int(input("[정수1]를 입력하세요 >>"))
num2 = int(input("[정수2]를 입력하세요 >>"))
num3 = int(input("[정수2]를 입력하세요 >>"))
num4 = int(input("[정수2]를 입력하세요 >>"))

class Calculator:
    # def __init__(self, cal_plus, cal_minus, cal_multiple, cal_divide):
    #     self.cal_plus = cal_plus
    #     self.cal_minus = cal_minus
    #     self.cal_multiple = cal_multiple
    #     self.cal_divide = cal_divide

    # 더하기
    def add(self, x, y):
        # self.cal_plus = cal_plus
        return x + y

    # 더하기
    def minus(self, x, y):
        # self.cal_minus = cal_minus
        return x - y  # 더하기

    def multiple(self, x, y):
        # self.cal_multiple = cal_multiple
        return x * y  # 더하기

    def divide(self, x, y):
        # self.cal_divide = cal_divide
        return x // y



# c1 = Calculator(num1, num2, num3, num4)
#
# cal_plus = c1.cal_plus()
# cal_minus = c1.cal_minus()
# cal_multiple = c1.cal_multiple()
# cal_divide = c1.cal_divide()

c1 = Calculator()
plus = c1.add(num1, num2)
minus =c1.minus(num1, num2)
multiple =c1.multiple(num1, num2)
divide =c1.divide(num1, num2)
print(" + ", plus)
print(" + ", minus)
print(" + ", multiple)
print(" + ", divide)
