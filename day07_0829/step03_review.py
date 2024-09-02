# 공통점 : 여러 자료들을 하나의 자료로 묶음
# 리스트 변수 = [요소1, 요소2]
# 튜플 변수 = (value1, value2)
# 딕셔너리 변수 = {key1 : value1, key2 : value2}
# 'americano', 5600, 'cafelatte', 6300, '자몽차', 5500
# 실습1 : 카페의 제품명과 가격을 컴퓨터에 저장하는 설계
# 그림과 같이 가격이 여러개 존재할 때 타입 생각 1
# 생각 1: 리스트 타입일때
# 생각 2ㅣ 튜플타입일때
# 생각 3 ㅣ 딕셔너리일때
# 생각 4 : 위의 3가지를 사용하지 못할 때
# 샘플 : 아메리카(5,6), 카페라떼(6,3) , 자몽차(5,6)

# List
menuList = ['americano', 5600, 'cafeLatte', 6300, '자몽차', 5500]
print("menuList = ", menuList)
productList = []
priceList = []
for i in range(len(menuList)) :
    if i % 2 == 0 :
        productList.append(menuList[i])
    else :
        priceList.append(menuList[i])
print()
print("productList = ", productList)
print("priceList = ", priceList)

print()
# tulple
menuList_tup = ('americano', 5600, 'cafeLatte', 6300, '자몽차', 5500)
print("menuList_tup = ", menuList_tup)
productList_t = []
priceList_t = []
for i in range(len(menuList_tup)) :
    if i % 2 == 0 :
        productList_t.append(menuList_tup[i])
    else :
        priceList_t.append(menuList_tup[i])
print()
print("productList_t = ", productList_t)
print("productList_t = ", priceList_t)
print()

# dic
menuList_dic = {'americano' : 5600, 'cafeLatte' : 6300, '자몽차' : 5500}
print("menuList_dic = ", menuList_dic)
