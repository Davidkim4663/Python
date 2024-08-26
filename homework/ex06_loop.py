# [문제1]
# [지문] 1부터 100까지 누적합계를 구하는데 누적합계가 1000초과 하면 중지 하고 누적합계 출력 하시오.
endnum = int(input("정수를 입력하세요 \n>> "))
i = 1
sum = 0
for i in range(1, endnum, i + 1):
    if sum >= 1000:
        print("1000을 초과 >> 종료")
        break

# [문제2]
# [지문]  키보드로 부터 무한 입력을 받아 입력받은 값을 출력하시오. 만약에 x 입력하면 반복문 종료 합니다.
while True:
    num = input("입력 >> ")
    stopLoop = num == "x"
    if stopLoop:
        print("집 보내줘")
        break
"""
# [문제3]
# [지문]   369 게임
# [출력조건]
#
# 1. 하나의 정수를 입력받아 해당 정수까지 숫자 출력
# 2. 3 혹은 6 혹은 9 가 포함되어 있는 수는 박수 출력
# 3. 1-> 1 , 1->2 , 3-> 박수 , 13-> 박수 , 33 -> 박수박수 , 36-> 박수박수
# """
scope = int(input("정수를 입력하세요 \n>> "))
i = 1
while i <= scope :
    checking_unit_ten = i // 10 == 3 or i // 10 == 6 or i // 10 == 9
    checking_unit_one = i % 10 == 3 or i % 10 == 6 or i % 10 == 9
    clap_twice = checking_unit_ten and checking_unit_one # 33,, 36, 39
    clap_once = checking_unit_ten or checking_unit_one # 30 31, 23 etc
    if clap_twice : print("박수박수")
    elif clap_once : print("박수")
    else : print(i)
    i += 1


"""
[문제4]
[지문]  키오스크 만들기1탄 , 아래 주어진 샘플코드를 조건에 따라 완성 하시오.

[조건]

[조건1] 무한루프
[조건2] 메뉴에서 번호를 클릭할때마다 제품을 각 장바구니 에 1개씩 담아줍니다.
		만일 콜라를 2번 선택하면 장바구니에 콜라 수량이 2개가 됩니다.
[조건3] 결제를 선택했을때 장바구니 제품명과 총수량 출력후 총금액을 출력한다.
		만일 결제를 했을경우 장바구니에 있는 수량만큼 재고를 차감합니다.
[조건5] 모든 제품의 초기 재고 10개 입니다. [ 재고 가 없을경우 판매 불가 ]
[조건6] 각 제품의 가격은 콜라(300원) 사이다(400원) 환타(500원) 입니다.

"""
# 지갑
myWallet = 10000

# 아이템 재고
inventory_Coke = 10
inventory_Sprite = 10
inventory_Fanta = 10

# 아이템 가격
item_Coke_price = 300
item_Sprite_price = 400
item_Fanta_price = 500

stock_quantity_Coke = 0  # 장바구니
stock_quantity_Sprite = 0  # 장바구니
stock_quantity_Fanta = 0  # 장바구니

cur_myItem = 0  # 현재 장바구니
payMent = 0

print("★ [음료수 키오스크] ★\n")
while True:
    kioskChoiceNumber = int(input("[1] 상품을 주문하기, [2] 종료하기\n>> "))
    kioskChoiceNumber_order = kioskChoiceNumber == 1
    kioskChoiceNumber_exit = kioskChoiceNumber == 2
    if kioskChoiceNumber_order:
        print(f"[메뉴판]\n[콜라 : {item_Coke_price}원, 사이다 : {item_Sprite_price}원, 환타 : {item_Fanta_price}원]\n")
        orderItem_input = int(input("주문하실 메뉴를 선택해주세요.\n >> [1] 콜라, [2] 사이다, [3] 환타\n>> "))
        print()
        # 콜라 주문
        if orderItem_input == 1:
            print("콜라를 선택하셨습니다.")
            orderQuantity = int(input("주문 하실 수량을 입력 하세요 >> "))
            print(f"선택하신 주문 건 = {orderQuantity}개\n")
            # 주문수 만큼 반복
            i = 1
            for i in range(i, (orderQuantity + 1), i):
                cur_myItem += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent = myWallet - payMent_total
                # 남은 재고 수량
                # inventory_Coke -= cur_myItem  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

                # 결제금액 확인
                print("====[ 장바구니 ]======\n")

                print(f"제품명 : 콜라\n결제금액={payMent_total}원 입니다.\n결제를 진행하시겠습니까??\n\n")
                askingForPay = input("결제를 원하시면 'yes'\n결제를 취소 하시려면 'no' 를 입력해주세요\n>> ")

                agreePayment_admin = askingForPay == "yes"
                disAgreePayment_admin = askingForPay == "no"
                checkingPayment = myWallet >= payMent  # 결제금액이 내 잔고보다 적을경우에 계산

                # 결제승인성공
                checkingPayment_admin = checkingPayment == True and agreePayment_admin == True

                # 결제실패(재고,잔고부족)
                checkingPayment_Fail = not checkingPayment_admin  # 결제금액이 적을 때
                checkingInventory_lack = inventory_Coke == 0 or (
                        orderQuantity > inventory_Coke)

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 콜라 재고량 = {inventory_Coke}, 고객요청 수량 = {orderQuantity}\n")
                    print("초기화면으로 돌아갑니다.")
                    break
                    # 결제금액이 현재잔고보다 적고 결제승인을 요청 했을 때

                if checkingPayment_admin:
                    print("결제를 진행 합니다 >> ")
                    print()
                    print()
                    print("결제승인이 완료되었습니다.")
                    print(f"[결제 영수증]\n 제품명 : 콜라\n 주문수량 = {orderQuantity}\n 주문금액 = {payMent_total} ")
                    break

        # 사이다 주문
        if orderItem_input == 2:
            print("사이다를 선택하셨습니다.")
            orderQuantity = int(input("주문 하실 수량을 입력 하세요 >> "))
            print(f"선택하신 주문 건 = {orderQuantity}개\n")
            # 주문수 만큼 반복
            i = 1
            for i in range(i, (orderQuantity + 1), i):
                cur_myItem += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent_coke = myWallet - payMent_total
                # 남은 재고 수량
                # inventory_Coke -= cur_myItem  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

                # 결제금액 확인
                print("====[ 장바구니 ]======\n")

                print(f"제품명 : 사이다\n결제금액={payMent_total}원 입니다.\n결제를 진행하시겠습니까??\n\n")
                askingForPay = input("결제를 원하시면 'yes'\n결제를 취소 하시려면 'no' 를 입력해주세요\n>> ")

                agreePayment_admin = askingForPay == "yes"
                disAgreePayment_admin = askingForPay == "no"
                checkingPayment = myWallet >= payMent_coke  # 결제금액이 내 잔고보다 적을경우에 계산

                # 결제승인성공
                checkingPayment_admin = checkingPayment == True and agreePayment_admin == True

                # 결제실패(재고,잔고부족)
                checkingPayment_Fail = not checkingPayment_admin  # 결제금액이 적을 때
                checkingInventory_lack = inventory_Coke == 0 or (
                        orderQuantity > inventory_Coke)

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent_coke}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 사이다 재고량 = {inventory_Coke}, 고객요청 수량 = {orderQuantity}\n")
                    print("초기화면으로 돌아갑니다.")
                    break
                    # 결제금액이 현재잔고보다 적고 결제승인을 요청 했을 때

                if checkingPayment_admin:
                    print("결제를 진행 합니다 >> ")
                    print()
                    print()
                    print("결제승인이 완료되었습니다.")
                    print(f"[결제 영수증]\n 제품명 : 사이다\n 주문수량 = {orderQuantity}\n 주문금액 = {payMent_total} ")
                    break

        # 환타 주문
        if orderItem_input == 3:
            print("환타를 선택하셨습니다.")
            orderQuantity = int(input("주문 하실 수량을 입력 하세요 >> "))
            print(f"선택하신 주문 건 = {orderQuantity}개\n")
            # 주문수 만큼 반복
            i = 1
            for i in range(i, (orderQuantity + 1), i):
                cur_myItem += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent_coke = myWallet - payMent_total
                # 남은 재고 수량
                # inventory_Coke -= cur_myItem  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

                # 결제금액 확인
                print("====[ 장바구니 ]======\n")

                print(f"제품명 : 환타\n결제금액={payMent_total}원 입니다.\n결제를 진행하시겠습니까??\n\n")
                askingForPay = input("결제를 원하시면 'yes'\n결제를 취소 하시려면 'no' 를 입력해주세요\n>> ")

                agreePayment_admin = askingForPay == "yes"
                disAgreePayment_admin = askingForPay == "no"
                checkingPayment = myWallet >= payMent_coke  # 결제금액이 내 잔고보다 적을경우에 계산

                # 결제승인성공
                checkingPayment_admin = checkingPayment == True and agreePayment_admin == True

                # 결제실패(재고,잔고부족)
                checkingPayment_Fail = not checkingPayment_admin  # 결제금액이 적을 때
                checkingInventory_lack = inventory_Coke == 0 or (
                        orderQuantity > inventory_Coke)

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent_coke}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 환타 재고량 = {inventory_Coke}, 고객요청 수량 = {orderQuantity}\n")
                    print("초기화면으로 돌아갑니다.")
                    break
                    # 결제금액이 현재잔고보다 적고 결제승인을 요청 했을 때

                if checkingPayment_admin:
                    print("결제를 진행 합니다 >> ")
                    print()
                    print()
                    print("결제승인이 완료되었습니다.")
                    print(f"[결제 영수증]\n 제품명 : 환타\n 주문수량 = {orderQuantity}\n 주문금액 = {payMent_total} ")
                    break

    elif kioskChoiceNumber_exit:
        print("키오스크를 종료합니다.")
        break
