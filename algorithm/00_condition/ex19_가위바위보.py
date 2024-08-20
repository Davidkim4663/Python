'''
[가위(0) 바위(1) 보(2) 게임]
	[1] com은 0~2 사이의 숫자를 랜덤 저장한다.
	[2] me는  0~2 사이의 숫자를 랜덤 저장한다.
	[3] 가위, 바위, 보를 0, 1, 2 숫자로 대신 표현한다.
	[4] com과 me를 비교해서 me를 기준으로 "비김" "승리" "패배"를 출력하시오.
'''
import random
com = random.randint(0, 2)
me = random.randint(0, 2)
print("0 : 가위, 1 : 바위, 2 : 보\n")
print("me = " + str(me) + ", com = " + str(com))

win_me = (me == 0 and com == 2) or (me == 1 and com == 0) or (me == 2 and com == 1)
win_com = (com == 0 and me == 2) or (com == 1 and me == 0) or (com == 2 and me == 1)
miss = me == com

if win_me : print("내가 이겼다.")
elif win_com : print("내가 졌다")
elif miss : print("비겼다")


