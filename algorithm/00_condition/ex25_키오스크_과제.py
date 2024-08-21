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
cash = 15000
# 버거세트 가격
beef_burgur = 20000
french_Frie = 2000
coke = 1500

setMenu_burger = beef_burgur + french_Frie + coke # 10,500

# 치킨세트 가격
crispy_Chicken= 15000
french_Frie = 2000
coke = 1500
setMenu_Chicken = crispy_Chicken + french_Frie + coke # 13,500

# keyosk menu
print("============ 버거킹 =========== ")
keyosk_order = int(input("원하시는 메뉴를 선택하세요\n [1] 먹고가기, [2] 포장하기, [3] 나가기\n"))
if keyosk_order == 1:
    print("매장식사를 선택 하셨습니다\n >> ")
    selection_menu = int(input("원하시는 메뉴를 선택하세요 >> [1] 버거세트, [2] 치킨세트\n>> "))
    if selection_menu == 1: 
        print("버거세트를 입력하셨습니다")
        print("[버거세트]\n 불고기버거(7000won), 후렌치프라이(2000won), 콜라(1500won)\n")
        asking_order = input("주문 하시겠습니까? yes or no\n")
        if asking_order == "yes" :
            print(f"주문 하실 금액은 총 {setMenu_burger} 입니다. ")
            pay_order = input("결제 하시겠습니까? yes or no\n")
            if pay_order == "yes" and cash > setMenu_burger : print("결제가 진행 중 입니다, \n 결제가 완료되었습니다\n즐거운 식사시간 되세요 :) ")
            elif cash < setMenu_burger : print(f"잔고부족으로 인해 결제오류가 되었습니다, 현재 잔고 = {cash-setMenu_burger}")
        elif asking_order == "no" : print("주문을 취소 하였습니다, 초기화면으로 돌아 갑니다.")
    if selection_menu == 2:
        print("치킨세트를 입력하셨습니다")
        print("[치킨세트]\n 크리스피치킨(10000won), 후렌치프라이(2000won), 콜라(1500won)\n")
        asking_order = input("주문 하시겠습니까? yes or no\n")
        if asking_order == "yes" :
            print(f"주문 하실 금액은 총 {setMenu_Chicken} 입니다. ")
            pay_order = input("결제 하시겠습니까? yes or no\n")
            if pay_order == "yes" and cash > setMenu_Chicken : print("결제가 진행 중 입니다, \n 결제가 완료되었습니다\n즐거운 식사시간 되세요 :) ")
            elif cash < setMenu_Chicken : print(f"잔고부족으로 인해 결제오류가 되었습니다, 현재 잔고 = {cash-setMenu_Chicken}")
        elif asking_order == "no" : print("주문을 취소 하였습니다, 초기화면으로 돌아 갑니다.")
elif keyosk_order == 2:
    print("포장하기를 선택 하셨습니다 >> \n")
    selection_menu = int(input("원하시는 메뉴를 선택하세요 >> [1] 버거세트, [2] 치킨세트\n>>"))
    if selection_menu == 1:
        print("버거세트를 입력하셨습니다")
        print("[버거세트]\n 불고기버거(7000won), 후렌치프라이(2000won), 콜라(1500won)\n")
        asking_order = input("주문 하시겠습니까? yes or no\n")
        if asking_order == "yes" :
            print(f"주문 하실 금액은 총 {setMenu_burger} 입니다. ")
            pay_order = input("결제 하시겠습니까? yes or no\n")
            if pay_order == "yes" and cash > setMenu_burger : print("결제가 진행 중 입니다, \n 결제가 완료되었습니다\n즐거운 식사시간 되세요 :) ")
            elif cash < setMenu_burger : print(f"잔고부족으로 인해 결제오류가 되었습니다, 현재 잔고 = {cash-setMenu_burger}")
        elif asking_order == "no" : print("주문을 취소 하였습니다, 초기화면으로 돌아 갑니다.")
    if selection_menu == 2:
        print("치킨세트를 입력하셨습니다")
        print("[치킨세트]\n 크리스피치킨(10000won), 후렌치프라이(2000won), 콜라(1500won)\n")
        asking_order = input("주문 하시겠습니까? yes or no")
        if asking_order == "yes" :
            print(f"주문 하실 금액은 총 {setMenu_Chicken} 입니다. ")
            pay_order = input("결제 하시겠습니까? yes or no")
            if pay_order == "yes" and cash > setMenu_Chicken : print("결제가 진행 중 입니다, \n 결제가 완료되었습니다\n즐거운 식사시간 되세요 :) ")
            elif cash < setMenu_Chicken : print(f"잔고부족으로 인해 결제오류가 되었습니다, 현재 잔고 = {cash-setMenu_Chicken}")
        elif asking_order == "no" : print("주문을 취소 하였습니다, 초기화면으로 돌아 갑니다.")
elif keyosk_order == 3 :print("다음에 만나요")







