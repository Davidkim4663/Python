'''
	[문제]
		철수와 민수는 가위바위보를 6회 하였다.
		가위(0) , 바위(1) , 보(2) 를 뜻한다.
		아래 배열은 각각 가위바위보를 낸 기록을 저장한 것이다.

		철수와 민수는 계단 50번째부터 게임을 시작하였다.
		민수는 게임을 모두 끝마치고 어디 있는지 구하시오.
		[규칙]
			이기면 5칸 올라간다.
			비기면 1칸 올라간다.
			지면 3칸 내려간다.
	[정답]
		48
'''

철수 = [0, 1, 2, 2, 1, 0]
민수 = [2, 1, 1, 2, 0, 1]
print("철수 = ", 철수)
print("민수 = ", 민수)

sicssor = 0
rock = 1
papers = 2

win_pos = 5
loss_pos = 3
miss_pos = 1

철수_위치 = 50
민수_위치 = 50
print("철수 위치 ", 철수_위치)
print("민수 위치 ", 민수_위치)
print()
print("===========================================")
for i in range(len(철수)):
    print()
    철수_win = (sicssor == 철수[i] and papers == 민수[i]) or (rock == 철수[i] and sicssor == 민수[i]) or (
                papers == 철수[i] and rock == 민수[i])
    민수_win = (sicssor == 민수[i] and papers == 철수[i]) or (rock == 민수[i] and sicssor == 철수[i]) or (
                papers == 민수[i] and rock == 철수[i])
    miss = 철수[i] == 민수[i]

    if 철수_win:
        print(f"<철수 = {철수[i]} vs 민수 = {민수[i]} = 철수 승리 = {철수_win}>")
        철수_위치 += win_pos
        민수_위치 -= loss_pos
        print(f"철수 현재 위치 = {철수_위치}\n민수 현재 위치 = {민수_위치}")
        print()

    if 민수_win:
        print(f"<철수 = {철수[i]} vs 민수 = {민수[i]} = 민수 승리 = {철수_win}>")
        철수_위치 -= loss_pos
        민수_위치 += win_pos
        print(f"철수 현재 위치 = {철수_위치}\n민수 현재 위치 = {민수_위치}")
        print()

    if miss:
        print(f"<철수 = {철수[i]} vs 민수 = {민수[i]} = 서로 비겼다 = {철수_win, 민수_win}>")
        철수_위치 += miss_pos
        민수_위치 += miss_pos
        print(f"철수 현재 위치 = {철수_위치}\n민수 현재 위치 = {민수_위치}")
print("===========================================")
