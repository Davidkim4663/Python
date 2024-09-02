"""
 딕셔너리 {}
 key와 value값으로 한쌍을 여러 개 저장하는 자료구조
 
 리스트의 단점 :
 저장된 순서번호(인덱스)와 요소(값)로 저장되는 구조
 인덱스는 숫자로 구성된 순서번호 이므로 대량의 인덱스는 사람이 식별하기 힘듬

 딕셔너리 형태 {}
 {key : value, key : value, key : value}
 key와 value를 콜론을 구분하여 한쌍을 이루는 여러 쌍을 중괄호로 감싼 형식
"""

# [1] 딕셔너리 선언
dic = {"name" : "pey", "phone" : "010-3944-5544", "birth" : 1110}
myName = dic["name"]
print("myname = ", myName)

myPhone = dic["phone"]
print("myPhone = ", myPhone)

myBrith = dic["birth"]
print("myBrith = ", myBrith)

# 딕셔너리 중첩
dic_double = {'a' : {'b' : 'c'}}
print("dic_double", dic_double)
dic_double_g = dic_double['a']
print(dic_double_g)

# 딕셔너리 추가
dic['addr'] = '인천시' # addr이라는 k
print(dic)
myAddr = dic['addr']
print("myAddr = ", myAddr)

# 딕셔너리 수정
dic['name'] = 'kim'
print(dic)

# 딕셔너리 삭제
del dic['addr']
print(dic)

# 딕셔너리 함수
# 1. key() : 리스트 내 모든 key들을 모아서 객체로 반환하는 함수
print(".key() = ", dic.keys())

# 2. list() : 리스트 타입으로 변환하는 함수
print(".list() : ", list(dic.keys()))

# 3. value() : 딕셔너리 내 모든 value들을 모아서 객체()로 반환해주는 함수
print(".value() : ,", dic.values())

# 4. item() : 딕셔너리 내에 모든 key와 value들을 튜플로 묶은 객체러 반환해주는 함슈
print(".items() = ", dic.items())

# 5. get('key') : 딕셔너리
print(" .get('key') = ", dic.get('phone'))

# 6. key in dic - key 값의 유무를 확인

print('name' in dic)
print('str' in dic)

# 7. len()
print("len() = ", len(dic))


