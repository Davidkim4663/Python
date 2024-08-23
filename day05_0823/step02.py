# """
# # 반복문
#  - 특정 조건에 따라 실행문을 반복한다.
#  - 특정 조건이 True 맞으면 반복, False이면 반복종료
# """
#
# # range(시작숫자, 끝 숫자) - 시작 숫자부터 끝 숫자 미만을 range 객체로 반환
# # range(시작숫자, 끝 숫자, 증감숫자) : 시작숫자부터 끝수 미만까지 증감수 만큼 증감하면서  range 객체를 반환
#
# # [1] range(숫자) - 숫자목록[리스트]을 생성해서 반환해주는 함수
# print(list(range(10)))
# print(list(range(10, 20)))
# print(list(range(10, 20, 2)))
#
# # [2] for문
# scope = range(1, 5)
# cnt = 0
# for i in scope :
#     print(i,end=" ")
#     if i % 2 == 0 :
#         print()
# print()
# scope = range(1,101,1)
# cnt = 0
# for i in scope :
#     print(i,end=" ")
#     if i % 10 == 0 :
#         print()
#
# # (3) 1 ~ 200까지 출력을 할건데
#
# print()
# scope = range(1,200,10)
# cnt = 0
# for i in scope :
#     print(i,end=" ")
#     if i % 10 == 0 :
#         print()
#
# # (4) 1 ~ 10까지의 총 누적합계 출력
# print()
# scope_1 = range(1, 11, 1)
# i = 1
# sum = 0
# for i in scope_1 :
#  print(i, end= " ")
#  sum += i
# print("\nsum = ", sum)
#
# # (5)
# print()
# scope_1 = range(1, 11, 1)
# i = 1
# even_sum = 0
# odd_sum = 0
# for i in scope_1 :
#  if i % 2 == 0 :
#   print(i, end= " ")
#   even_sum += i
#  if i % 2 != 0 :
#   print(i, end= " ")
#   odd_sum += i
# print("\n짝수 sum = ", even_sum)
# print("\n홀수 sum = ", odd_sum)


sum = 0  # 모든 누적 합계를 저장 할 변수
for var in range(1, 11, 1):
    sum += var
    # print (f'sum: {sum}')
print(f'sum: {sum}')

var = 1  # 초기값 1 설정
sum = 0
for var in range(1, 11, 1):
    if var % 2 == 0:  # 짝수, == 1이면 홀수
        print(var, end=" ")  # end= " " -> 수평으로 출력
        sum += var  # 복합대입연산자 -> 반복문 돌면서 합계 저장
print("sum = ", sum)
