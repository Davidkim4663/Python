# 리스트와 관련된 주요 함수들

# 1. insert() - 리스트 내 지정한 인덱스 위치에 요소 값을 추가한다. (시작요소)
a = [1, 2, 3]
b = [4, 5, 6]
# a.insert(0, 0)
# print(a)


# 2. pop() : 리스트 내에 마지막 인덱스 요소를 삭제 # a.pop()
# print(a)

# 3. .count(찾을 요소 값) : 리스트 내 지정한 요소 값
# print(a.count(3))

# 4. .index(찾을 요소 값) : 리스트 내 지정한 요소 값이 위치한 인덱스 번호 반환
# print(a.index(2))

# a.extend(b)
# print("a = ", a)

# 5 .sort() : 리스트 내 요소들을 오름차순으로 정렬
# a.sort()
# print(a) # [2,3,10,20,30]
#
# # 6 .reverse() : 리스트 내 요소들을 내림차순으로 정렬
# a.reverse()
# print(a) # [2,3,10,20,30]

아파트 = [
    [101, 102, 103],
    [104, 105, 106],
    [107, 108, 109],
]

print('아파트', 아파트, "\n")

for i in 아파트:
    for j in i:
        print(j, end=" ")
    print()
