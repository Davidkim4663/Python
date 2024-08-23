# # 반복문 실습 1
# i = 1
# for i in range(2, 10, 1):
#     print("\n[ ", i, "]단")
#     for j in range(1, 10, 1):
#         print(i, " * ", j, " = ", (i * j))
#
# # 반복문 실습 2 : 키보드로부터 끝 값을 입력 받아 1부터 끝값까지 반복 출력
# # 홀수 일 때만
# endnum = int(input("정수를 입력하세요 \n>> "))
# i = 1
# sum = 0
# for i in range(1, endnum, i + 1):
#     if i % 2 != 0:
#         print(i, end=" ")
#         sum += i
#         if sum >= 1000 :
#             print("1000을 초과 >> 종료")
#             break
#
# print()
# print("\nsum = ", sum ^ 2)

# 반복문 실습 3 : 키보드로부터 끝 값을 입력을 무한루프로 받아서 만약에 x이면 무한 반복을 종료
while True :
    num = input("입력 >> ")
    stopLoop = num == "x"
    if stopLoop :
        print("집 보내줘")
        break
    
