# [1] 리스트 특정 요소의 값 수정, 인덱싱
memberList = ["이강인", "손흥민", "김민재"]
memberList[1] = "리오넬 메시"
print(memberList)

# [2] 리스트와 반복문 관계
# (1) 리스트 내 모든 요소들의 값 출력
# (2) 반복코드
for idx in range(0, len(memberList)):
    print(memberList[idx], end=" ")

for value in memberList:  # 리스트내 요소 값 * 하나씩 * 반복변수(value)에 대한 반복 # ㅁ
    print(value)

# (2)
marks = [95, 25, 67, 40, 80]  # 리스트
for i in range(len(marks)):
    # print(f" index = {i} ", marks[i], end=" ")
    if marks[i] < 60 :
        continue
    print(f" {[i]} 는 60점 이상 이므로 합격입니다.")

# (3) 리스트 컴프리헨션 사용
a = [py * 2 for py in range(0, 3)]
print(a)

b = [2*곱 for 곱 in range(1, 10)]
print(b)

c = [value for 곱 in range(1, 10)]

# (4) 2차원 리스트 : 리스트 타입에 리스트 타입을 저장하는 구조
d = [[1,2,3], [4,5,6]] # [[]]
# print(d[0])
# print(d[1])
#
# 0행 0열(1),1열(2),2열(3)
# print(d[0][0])
# print(d[0][1])
# print(d[0][2])
# print()
# 1행 0열(4),2열(5), 3열(6)
# print(d[1][0])
# print(d[1][1])
# print(d[1][2])
쇼핑백 = ['과자1', '음료1', '빵1']
# 2차원 리스트 인덱싱

아파트 = [
         [101, 102, 103],
         [104, 105, 106],
         [107, 108, 109],
                          ]
print("1층,",아파트[0][1]) 
print("1층,",아파트[1][2])
print("1층,",아파트[2][0])

# 2차원 리스트를 반복문과 사용
for 행 in 아파트 :
    print("행")
    for 열 in 행 : 
     print(열)








