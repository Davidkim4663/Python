'''
	[문제]
		아래 candy 리스트는 각 병에 들어있는 사탕의 양이다.
		한 사람당 한 병에서 25개씩 나눠주려 한다.
		나눠줄 수 있는 사람 수를 count 배열에 저장하시오.
		나눠주고 남은 사탕은 remainder 배열에 순차적으로 저장하시오.
	[정답]
		candy	 	[80, 53, 36, 22]
		count		[3, 2, 1, 0]
		remainder 	[5, 3, 11, 22]
'''

candy = [80,53,36,22]
count = []
remainder = []

candyCount = 0
remainderCount = 0

for i in range(len(candy)) :
    candyCount = candy[i] // 25
    remainderCount = candy[i] % 25
    count.append(candyCount)
    remainder.append(remainderCount)
print("candy = ", candy)
print("count = ", count)
print("remainder = ", remainder)
