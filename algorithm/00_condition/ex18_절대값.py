'''
랜덤 값 (1~10) 두 개를 저장한다.
앞의 숫자에서 뒤에 숫자를 뺀다.
만약에 값이 음수라면 양수로 변환해서 출력하시오.
'''
import random
randNum1 = random.randint(1, 10)
randNum2 = random.randint(1, 10)

randNum_calc = randNum1 - randNum2
if randNum_calc < 0 : randNum_calc = -randNum_calc
print(randNum_calc)