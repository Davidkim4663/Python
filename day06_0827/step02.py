# [1] 리스트의 연산
a = [1, 2, 3]
b = [4, 5, 6]
print("a = ", a)
print("b = ", b)
print(a + b)

total_a = 0
total_b = 0
sum = 0
total = []
for i in range(len(a)) :
    total_a += a[i]

for i in range(len(b)) :
    total_b += b[i]

print("total_a = ", total_a)
print("total_b = ", total_b)

for i in range(len(a)) :
    sum = a[i] + b [i]
    total.append(sum)
print("total = ", total)

# 리스트와 관련된 주요 함수들
# 1. append() - 리스트 값 추가 (마지막 요소)
# 2. insert() - 리스트 내 지정한 인덱스 위치에 요소 값을 추가한다. (시작 요소)
# 3. remove() - 리스트 값 제거
a.insert(0,5)
print(a)
a.remove(5)
print(a)

#4. pop () 또는 .pop(인텍스) :  리스트내 마지막 인덱스 요소를 삭제 한다 , 또는 지정한 인덱스의 요소를 삭제한다
# a.pop()
print(a) # [1,2,3]
# a.pop(1) # [1,2,3]

# 5 .count(찾을 요소 값) : 리스트 내 지정한 요소 값이 존재하는 개수 반환
print(a.count(3))
print(a.count(10))

# 6 .index(찾을 요소 값) :리스트 내 지정한 요소 값이 위치한 인덱스  번호 반환
print(a.index(3)) # 1 리스트 내 3이라는 자료가 1번 인덱스 위치에 있다는 뜻

# 7. extend(리스트) : 리스트 내 지정한 리스트를 (연결) 더 해준다
b = [10, 20]
a.extend(b) # 리스트 1. extend(리스트 2) : 리스트 2의 요소들을 리스트 1에 연장한다.
print(a) #

# 8 .sort() : 리스트 내 요소들을 오름차순으로 정렬
a.sort()
print(a) # [2,3,10,20,30]

# 9 .reverse() : 리스트 내 요소들을 내림차순으로 정렬
a.reverse()
print(a) # [2,3,10,20,30]

# 10 .len(리스트) : 지정한 리스트의 요소 개수 변환 함수
print(len(a))


