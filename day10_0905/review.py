# class
"""
ex) 시나리오
    # 오프라인 쇼핑은 내가 직접 가게에 가서 제품을 확인 구매
    # 온라인 쇼핑몰 손님 [사람], 설계(이름, 주소), 제품[신발]설계(제품명, 가격, 사진)

"""
class Member :
    def __init__(self, user_id, user_pw, check_pw, user_name, user_addr):
        self.user_id = user_id
        self.user_pw = user_pw
        self.check_pw = check_pw
        self.user_name = user_name
        self.user_addr = user_addr

memberList = Member("ip4523", "David452312!", "David452312!", "David", "서울 특별시 강남구 도산대로")

user1_id = memberList.user_id
user1_pw = memberList.user_pw
user1_check_pw = memberList.check_pw
user1_name = memberList.user_name
user1_addr = memberList.user_addr

checking_pw = user1_pw == user1_check_pw
checking_str = " "
if checking_pw :
    checking_str = "비밀번호 확인완료"
else :
    checking_str = "비밀번호 확인실패"

print(f"ID : {user1_id }\nPW : {user1_pw}\nPW_CHECKING : {checking_str}\nuser1_name :{user1_name}\nuser1_addr : {user1_addr}")


