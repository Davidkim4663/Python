# [문제1]
# [지문]  가위바위보 게임 구현하기.
# [조건] 가위가 '0' 이고 바위가 '1' 이고 보가 '2' 일때 플레이어1와 플레이어2 가 있습니다. 승리자 판단과 무승부 경우의수를 출력하시오.
import random
print("[ 가위바위보 게임]")
askingJoin = int(input("게임을 시작 하시겠습니까? [1] Play [2] Quit\n"))
if askingJoin == 1:
    print("GameStart >> 가위[0], 바위[1], 보[2] ")
    player_Com = random.randint(0, 2)  # 0 ~ 2
    i = 1
    while True:
        player_Me = random.randint(0, 2)  # 0 ~ 2
        print(f"안 내면 진다 가위바위보 ! com = {player_Com}, me = {player_Me}")

        matchResult_me_win = (player_Me == 0 and player_Com == 2) or (player_Me == 1 and player_Com == 0) or (
                player_Me == 2 and player_Com == 1)
        matchResult_com_win = (player_Com == 0 and player_Me == 2) or (player_Com == 1 and player_Me == 0) or (
                player_Com == 2 and player_Me == 1)
        matchResult_eachotherMiss = player_Com == player_Me
        miss_cnt = 0  # 계속 비길 때
        if matchResult_eachotherMiss:
            miss_cnt += 1
            if miss_cnt == 3:
                print(f"게임을 다시 합니다.")
                continue
            elif miss_cnt < 3:
                print(f"비겼다 >>\n승부결과 : com = {player_Com}, me = {player_Me}")
                break
        if matchResult_me_win:
            print(f"축하합니다, 당신이 이겼습니다.\n승부결과 : com = {player_Com}, me = {player_Me}")
            reTry_me = input("재도전 하시겠습니까? [0] yes, [1], no")
            if reTry_me == 0:
                continue
            elif reTry_me == 1:
                print("게임을 종료 합니다")
                break
        if matchResult_com_win:
            print(f"Game Over >> 재도전 하시겠습니까?\n승부결과 : com = {player_Com}, me = {player_Me}")
            reTry_me = input("재도전 하시겠습니까? [0] yes, [1], no")
            if reTry_me == 0:
                print("게임을 다시 시작 합니다.")
                continue
            elif reTry_me == 1:
                print("게임을 종료 합니다")
                break
    i += 1
elif askingJoin == 2:
print("게임을 종료합니다.")
# [입력 조건]
#
# 플레이어1 과 플레이어2 에게 각각 0 또는 1 또는 2 를 입력을 받습니다.
# [출력 조건]
#
# 플레이어1 이기면 ' 플레이어1 승리 ', 플레이어2 이기면 ' 플레이어2 승리 ' 무승부 이면 '무승부' 출력 하시오.

# [문제2]
# [지문]  윤년/평년 판단하기
# [계산식]
# -연수가 4로 나누어 떨어지는 해는 윤년으로 한다.
# -연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다.
# -연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다.
# [입력 조건]
#  하나의 연도를 입력 받습니다.
# [출력 예시]
year = int(input("연도를 입력 하세요 \n>>"))
leapYear = year % 4 == 0 and year % 400 == 0
commonYear = not leapYear
if leapYear:
    print(f"{year} => 윤년 입니다")
elif commonYear:
    print(f"{year} => 평년 입니다")

# [문제3]
# [지문]  로그인 처리
# [입력 조건]
#
# 아이디[문자열] 와 비밀번호[문자열] 를 입력받기
# [출력 조건]
#
# 1. 아이디가 'admin' 이고 비밀번호가 '1234' 모두 동일하면 '로그인성공'
# 2. 아이디가 다르면 '아이디 정보가 일치하지 않습니다.'
# 3. 아이디는 일치하고 비밀번호가 다르면 '비밀번호 정보가 일치하지 않습니다'

insertId = input("아이디를 입력 하세요 \n>> ")
insertPw = input("비밀번호를 입력 하세요 \n>> ")
userId = 'admin'
userPw = '1234'

passID = insertId == userId
passPw = insertPw == userPw
loginSuccess = passID == True and passPw == True
if loginSuccess:
    print("로그인 성공")
else:
    print("로그인 실패")

# [문제4]
# [지문]  당첨번호 개수  찾기
# [선언 변수 조건]  공1 = 14 ; 공2 = 21 ; 공3 = 9; 이와 같이 변수를 먼저 선언해주세요.
#
# [입력 조건]
#
# 세개의 정수를 입력받아 각 변수에 저장하시오.
# [출력 조건]
#
# 입력받은 세 정수 중에서 공1~공3 까지 동일한 번호 가 몇개 인지 출력하시오.
ball1 = int(input("공[1] 번호를 입력하세요 >> "))
ball1_num = ball1

ball2 = int(input("공[2] 번호를 입력하세요 >> "))
ball2_num = ball2

ball3 = int(input("공[3] 번호를 입력하세요 >> "))
ball3_num = ball3
i = 1
cnt = 0
print()
while True :
    player1 = random.randint(1, 30)
    player2 = random.randint(1, 30)
    player3 = random.randint(1, 30)
    checkingSame_num1 = ball1_num == player1
    checkingSame_num2 = ball2_num == player2
    checkingSame_num3 = ball3_num == player3

    checkingTotal = (checkingSame_num1 == True) and (checkingSame_num2 == True) and (checkingSame_num3 == True)
    if checkingTotal :
        cnt += 1
        if cnt == 5 :
            print(f"공[1] = [{ball1} : {player1}]\n공[2] = [{ball2} : {player2}]\n공[3] = [{ball3} : {player3}] ")
            print("맞췄다!")
            break
        else : continue
i += 1

