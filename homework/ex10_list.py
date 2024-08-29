myWallet = 10000

# 아이템 재고
# inventory_Coke = 10
# inventory_Sprite = 10
# inventory_Fanta = 10

# 아이템 재고
inventory = [10, 10, 10]

# 아이템 가격
item_Coke_price = 300
item_Sprite_price = 400
item_Fanta_price = 500

# 장바구니
cart = [0, 0, 0]

# cur_myItem = 0  # 현재 장바구니
payMent = 0

print("★ [음료수 키오스크] ★\n")
while True:
    kioskChoiceNumber = int(input("[1] 상품을 주문하기, [2] 종료하기\n>> "))
    kioskChoiceNumber_order = kioskChoiceNumber == 1
    kioskChoiceNumber_exit = kioskChoiceNumber == 2
    errorMessage = not kioskChoiceNumber_order and not kioskChoiceNumber_exit
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
                cart[i] += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent = myWallet - payMent_total
                # 남은 재고 수량
                cur_inventory = inventory[i] - cart[i]  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

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
                checkingInventory_lack = inventory[i] == 0 or (
                        orderQuantity > inventory[i])

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 콜라 재고량 = {cur_inventory}, 고객요청 수량 = {orderQuantity}\n")
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
        elif orderItem_input == 2:
            print("사이다를 선택하셨습니다.")
            orderQuantity = int(input("주문 하실 수량을 입력 하세요 >> "))
            print(f"선택하신 주문 건 = {orderQuantity}개\n")
            # 주문수 만큼 반복
            i = 1
            for i in range(i, (orderQuantity + 1), i):
                cart[i] += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent = myWallet - payMent_total
                # 남은 재고 수량
                cur_inventory = inventory[i] - cart[
                    i]  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

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
                checkingInventory_lack = inventory[i] == 0 or (
                        orderQuantity > inventory[i])

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 콜라 재고량 = {cur_inventory}, 고객요청 수량 = {orderQuantity}\n")
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

        # 환타 주문
        elif orderItem_input == 3:
            print("환타를 선택하셨습니다.")
            orderQuantity = int(input("주문 하실 수량을 입력 하세요 >> "))
            print(f"선택하신 주문 건 = {orderQuantity}개\n")
            # 주문수 만큼 반복
            i = 1
            for i in range(i, (orderQuantity + 1), i):
                cart[i] += 1  # ex 2개
                # 결제금액
                payMent_total = item_Coke_price * orderQuantity
                # 잔고 금액
                payMent = myWallet - payMent_total
                # 남은 재고 수량
                cur_inventory = inventory[i] - cart[
                    i]  # ex) inventory_Coke(10) -= 2 inventory_Coke 8 재고수량이 8개 남고, 아이템 수는 증가

                # 결제금액 확인
                print("====[ 장바구니 ]======\n")

                print(f"제품명 : 환타\n결제금액={payMent_total}원 입니다.\n결제를 진행하시겠습니까??\n\n")
                askingForPay = input("결제를 원하시면 'yes'\n결제를 취소 하시려면 'no' 를 입력해주세요\n>> ")

                agreePayment_admin = askingForPay == "yes"
                disAgreePayment_admin = askingForPay == "no"
                checkingPayment = myWallet >= payMent  # 결제금액이 내 잔고보다 적을경우에 계산

                # 결제승인성공
                checkingPayment_admin = checkingPayment == True and agreePayment_admin == True

                # 결제실패(재고,잔고부족)
                checkingPayment_Fail = not checkingPayment_admin  # 결제금액이 적을 때
                checkingInventory_lack = inventory[i] == 0 or (
                        orderQuantity > inventory[i])

                # 결제실패 했을 때
                if checkingPayment_Fail:  # 결제금액이 부족할 때
                    print()
                    print(">>> 결제승인 오류 <<< : 잔고가 부족합니다. \n")
                    print(f"결제 할 금액 = {payMent}, 현재 내 잔고 = {myWallet}")
                    print("초기화면으로 돌아갑니다.")
                    break

                if checkingInventory_lack:  # 재고량이 부족할 때
                    print(">>> 결제승인 오류 <<< : 재고가 부족합니다. \n")
                    print(f"현재 환타 재고량 = {cur_inventory}, 고객요청 수량 = {orderQuantity}\n")
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
    elif errorMessage :
        print("잘못 입력하셨습니다.")
