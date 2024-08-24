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
[문제3]
[지문]   369 게임
[출력조건]

1. 하나의 정수를 입력받아 해당 정수까지 숫자 출력
2. 3 혹은 6 혹은 9 가 포함되어 있는 수는 박수 출력
3. 1-> 1 , 1->2 , 3-> 박수 , 13-> 박수 , 33 -> 박수박수 , 36-> 박수박수
"""
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
