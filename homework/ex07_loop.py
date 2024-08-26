"""
[문제1]
[지문] 양의 정수를 입력받아, 해당 숫자만큼의 줄에 걸쳐 별(*)을 출력하는 프로그램을 작성하세요. 예를 들어, 사용자가 5를 입력하면 다음과 같이 출력되어야 합니다.
[출력 예시]
*
**
***
****
*****
"""

print("[문제 1] 직각삼각형")
ex1_num = int(input("숫자 입력\n>>"))
for i in range(ex1_num):
    for j in range(i + 1):
        print("★", end=" ")
    print()
"""
[문제2]
[지문] 양의 정수를 입력받아, 해당 숫자만큼의 줄에 걸쳐 별(*)을 출력하는 프로그램을 작성하세요. 예를 들어, 사용자가 5를 입력하면 다음과 같이 출력되어야 합니다.
[출력 예시]
    *****
    ****
    ***
    **
    *
"""
print()
ex2_num = int(input("숫자 입력\n>>"))
print("[문제 2] 역직각삼각형")
for i in range(ex2_num):
    for j in range(ex2_num - i):
        print("★", end=" ")
    print()

"""
[문제3]
[지문] 양의 정수를 입력받아, 해당 숫자만큼의 줄에 걸쳐 별(*)을 출력하는 프로그램을 작성하세요. 예를 들어, 사용자가 5를 입력하면 다음과 같이 출력되어야 합니다.
[출력 예시]
     *
    **
   ***
  ****
 *****
"""
print()
print("[문제 3] 직각삼각형(반대) ")
ex3_num = int(input("숫자 입력\n>>"))
for i in range(ex3_num):
    for j in range(ex3_num - (i + 1)):
        print(" ", end=" ")
    for k in range(i + 1):
        print("★", end=" ")
    print()

"""
[문제4]
[지문] 양의 정수를 입력받아, 해당 숫자만큼의 줄에 걸쳐 별(*)을 출력하는 프로그램을 작성하세요. 예를 들어, 사용자가 5를 입력하면 다음과 같이 출력되어야 합니다.

[출력 예시]
*****
 ****
  ***
   **
    *
"""
print()
print("[문제 4] 역직각삼각형(반대)")
ex4_num = int(input("숫자 입력\n>>"))
for i in range(ex4_num):
    for j in range(i):
        print(" ", end=" ")
    for k in range(ex4_num - i):
        print("★", end=" ")
    print()

"""
[문제5]
[지문] 양의 정수를 입력받아, 해당 숫자만큼의 줄에 걸쳐 별(*)을 출력하는 프로그램을 작성하세요. 예를 들어, 사용자가 5를 입력하면 다음과 같이 출력되어야 합니다.
[출력 예시]
    *
   ***
  *****
 *******
*********
"""
print()
print("[문제 5] 정삼각형 ")
ex5_num = int(input("숫자입력 >> "))
for i in range(1, ex5_num + 1) :
    for j in range (ex5_num - i) :
        print(" ",end=" ")
    for k in range (i * 2 - 1) :
           print("*",end=" ")
    print()


