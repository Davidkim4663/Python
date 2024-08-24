# [문제1]
# [지문]  반복문을 이용하여 '야호' 100번 출력하시오.
from random import random

print("[문제 1]]\n")
i = 1
for i in range(1, 101, i):
    print(i, " 야호", end=" ")
    if i % 5 == 0:
        print()

# [문제2]
# [지문]  두 개의 정수를 입력받아서, 두 수 사이의 모든 정수를 출력하는 프로그램을 작성하세요. (단, 입력받은 두 수도 포함)
print("[문제 2]]\n")
oneNumber = int(input("1. 정수를 입력 하세요 \n>> "))
anotherNumber = int(input("2. 정수를 입력 하세요 \n>> "))
i = 1
for i in range(oneNumber, (anotherNumber+1), i) :
    print(i,end=" ")

# [문제3]
# [지문] 하나의 반복횟수를 입력받아서, 입력받은 반복횟수만큼 반복을 하여 반복적으로 정수를 입력받아서,
# 입력받은 정수들의 누적합계를 구합니다.
print("[문제 3]]\n")
someNumber = int(input("반복 횟수를 입력하세요 \n>> "))
sum = 0
i = 1
for i in range(i, (someNumber+1)) :
    print(i, end= " ")
    sum += i
print("\n합계 = ", sum)

# [문제4]
# [지문]  2~9단 에서 3단을 제외한 구구단을 구현하시오.
print("<< 구구단을 외우자 >>")
choice = int(input("원하시는 구구단을 선택하세요\n [1] 구구단 게임, [2] 구구단 학습]\n >> "))
if choice == 1:
    print(">> 1. [구구단 게임] <<")
    i = 1
    while True:
        insertCoin = int(input("게임 시작을 원하시면 코인을 넣어주세요 \n>> [1] 0 (play), [2] 1 (exit)\n insertCoin = "))
        playGame = insertCoin == 0
        exitGame = insertCoin == 1
        insertError = not playGame and not exitGame
        if playGame:
            print("게임을 시작합니다.\n")
            print("2단 부터 9단 중 희망 하시는 단을 입력하세요\n")
            insert_gugudan_x = int(input("단 입력 \n>> "))
            gugudan_x = insert_gugudan_x
            gugudan_y = 9
            i = 1
            for i in range(gugudan_x, (gugudan_y + 1), i):
                print(f"<< {gugudan_x} 단 >> ]\n")
                j = 1
                for j in range(1, (gugudan_y + 1), j):
                    print(gugudan_x, " * ", j, " = ", (gugudan_x * gugudan_y))
                if j >= 9:
                    print("=====[End]======")
                    oneMoreTime = ("게임을 더 원하시면 코인을 넣어주세요")
                    break
        elif insertError:
            print("잘못 입력하셨습니다, 다시 입력해주세요\n")
            continue

        elif exitGame:
            print("게임을 종료합니다, 감사합니다.")
            break
if choice == 2:
    print(">> 2. [구구단 학습하기] <<\n")
    k = 2
    for k in range(k, 10):
        if k != 3:
            print("[", k, "단 ]")
            h = 1
            for h in range(1, 10):
                print(k, " * ", h, " = ", (k * h))
