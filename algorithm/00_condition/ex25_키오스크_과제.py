'''
[키오스크]
	철수는 햄버거 가게를 운영한다.
	가게 내에 키오스크를 설치하고 잘 작동하는지 테스트하고 있다.
	랜덤으로 번호를 선택하고 아이템과 현금을 비교 후 결과를 출력하시오.

	해당 상품 가격이 현금보다 적으면, 현금에서 차감하고 구입 메세지를 출력하시오.
	해당 상품 가격이 현금보다 클 경우, "구입불가" 메세지를 출력하시오.
'''
import random
# cash
cash = 50000

# keyosk menu
print("============ 버거킹 =========== ")
order_selection = random.randint(0, 1)
take_in = order_selection == 0 # 먹고가기
take_out = order_selection == 1 # 포장하기

# menu
if take_in : print("매장식사를 선택하셨습니다.")






