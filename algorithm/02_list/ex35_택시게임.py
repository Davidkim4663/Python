'''
	[문제]
		현재 택시는 5 , 5 위치에 있다. (y = 5 , x = 5)
		dir 배열은 뱡향을 뜻하고 [0, 1, 2 ,3] 은 [북, 동, 남, 서] 를 뜻한다.
		speed 배열은 속도를 뜻한다.
		dir 과 speed 배열은 택시가 매번이동한 내용을 기록한 것이다.
		dir 과 speed 를 다 적용하면 y 와 x 는 어디에 와있는지 출력하시오.

	[정답]
		dir = 3 , speed = 4 : 서쪽으로 4칸이므로 x에서 4를 뺀다.
		dir = 2 , speed = 3 : 남쪽으로 3칸이므로 y에서 3을 뺸다.
		dir = 1 , speed = 1 : 동쪽으로 1칸이므로 x에서 1을 더한다.
		dir = 0 , speed = 2 : 북쪽으로 2칸이므로 y에서 2를 더한다.
		dir = 1 , speed = 3 : 동쪽으로 3칸이므로 x에서 3을 더한다.

        y = 4
        x = 5
'''
y = 5
x = 5

dir = [3, 2, 1, 0, 1]
speed = [4, 3, 1, 2, 3]

print(">>>>>>> [택시게임] <<<<<<<")
print("dir = ",dir)
print("speed = ", speed)
print("북 = 0, 동 = 1, 남 = 2, 서 = 3\n")
print(f'현재 위치 : x = {x}, y = {y}')
print()
# for i in range(len(dir)) :
dir_west = 3
dir_north = 0
dir_east = 1
dir_south = 2

for i in range(len(dir)) :
    west = dir_west == dir[i]
    north = dir_west == dir[i]
    east = dir_east == dir[i]
    south = dir_south == dir[i]
    if west :
        x -= speed[i] # 서쪽일 때
        print(f"dir = {dir[i]}, speed = {speed[i]} : 서쪽으로 {speed[i]}칸 이므로 x에서 {speed[i]}를 뺀다")
        print("현재 위치 x = ",x, ",y = ",y)
        print()
    if east :
        x += speed[i] # 동쪽일 때
        print(f"dir = {dir[i]}, speed = {speed[i]} : 동쪽으로 {speed[i]}칸 이므로 x에서 {speed[i]}를 더한다")
        print("현재 위치 x = ",x, ",y = ",y)
        print()

    if north :
        y += speed[i] # 북쪽일 때
        print(f"dir = {dir[i]}, speed = {speed[i]} : 북쪽으로 {speed[i]}칸 이므로 y에서 {speed[i]}를 더한다")
        print("현재 위치 x = ",x, ",y = ",y)
        print()

    if south :
        y -= speed[i]
        print(f"dir = {dir[i]}, speed = {speed[i]} : 남쪽으로 {speed[i]}칸 이므로 y에서 {speed[i]}를 뺀다")
        print("현재 위치 x = ",x, ",y = ",y)
        print()

print()
print("현재 위치 x = ",x, ",y = ",y)
