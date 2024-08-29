"""
 딕셔너리 {}
 key와 value 값으로 한쌍으로 여러 개를 저장하는 자료구조
 why?
    리스트의 부족한점
     - 저장된 순서번호 (인덱스)와 요소(값) 저장되는 구조
     - 인덱스는 숫자로 구성된 순서번호이므로 대량의 인덱스는 사람이 식별하기 어렵다
     

 딕셔너리 형태 {} 
  {key : value, key : value, key : value, key : value}
   key와 value를 클론으로 구분하여 한쌍을 이루는 여러 쌍을 중괄호로 감싼 형식

"""
from os import remove

# [1] 딕셔너리 선언
dic = {'name': 'pey', 'phone': '010-9233-4663', 'birth': 1110}

dic2 = {1: "hi"}

dic3 = {'a': {'b': 'h2'}}  # 딕셔너리 안에 중첩이 가능함

dic4 = {'a': [1, 2, 3]}  # 'a'라는 key에 리스트 자료가 1개(value)가 존재한다.
print(dic4)

# [2] 딕셔너리의 한쌍 추가(변수명['key'] = 값) 및 삭제
#  만약에 key가 존재하면 수정, 존재하지 않으면 추가
#  추가
dic['addr'] = '인천시'  # dic(딕셔너리)에 'addr'이라는 key와 '인천시'라는 value를 한쌍으로 해서 딕셔너리를 저장
print(dic)

# 수정
dic['name'] = 'kim'
print(dic)

# 한쌍 삭제 del 변수명['deleteKey']
del dic['addr']  # del 키워드[키워드란 언어에서 기능이 담긴 단어 ]
print("삭제 후(dic)", dic)

# [3] 딕셔너리 만들 때 주의할 점
# a = {1: 'a', 1: 'b'}
# 중복된 key의 이름을 가질 수 없는데, key는 여러 쌍들 중에 value의 구분 용도로 사용하기 때문에
# 리스트(객체) 타입으로는 key를 사용할 수 없다.
# a = {[1, 2]: 'h1'}

# 딕셔너리에서 key를 이용한 value 추출 변수명['key']
print(dic['name'])
mytel = dic['phone']
print(mytel)

# 존재하지 않는 key 값을 호출 시 에러발생
# print(dic['age'])


# [5] 딕셔너리의 관련된 함수(입력에 따른 기능을 처리 후 결과를 반환하는 함수)들
#  print('aa')

"""
딕셔너리 함수
"""
print()
# 1. .keys() : 딕셔너리 내 모든 key들을 모아서 객체로 반환하는 함수
print(".keys() : ", dic.keys())

# 2, .list() : 리스트 타입으로 변환하는 함수
print(".list() : ", list(dic.keys()))

# 3. .value() : 딕셔너리 내 모든 value들을 모아서 객체()로 반환해주는 함수
print("..values() : ", dic.values())

# 4.
print("list(dic.values()) = ", list(dic.values()))

# 5, items() : 딕셔너리 내 모든 쌍(key : value)들을 튜플로 묶은 객체로 반환해주는 함수
print(".items() = ", dic.items())

# 6.
print(list(dic.items()))

# 7.  .get('key') : 딕셔너리 내 key에 해당하는 value를 반환하는 함수\
print(" .get('key') = ", dic.get('name'))

print(" .get('key') = ", dic.get('age')) # 딕셔너리 내 존재하지 않는 key를 호출하면 none으로 반환

# 8. key in 딕셔너리
print('name'in dic)
print('age' in dic)

# 9. len()
print("len()  = ", len(dic)) # 요소 내의 개수