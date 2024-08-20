'''
	[문제]
		[1] 0에서 100 사이의 랜덤 점수 2개를 저장해 평균을 구한다.
		[2] 평균이 60점 이상이면 합격, 60점 미만이면 불합격이다.
		[3] 단, 평균이 60 이상이라도, 한 과목이라도 50 미만이면 불합격을 출력하시오.
'''
import random

score1 = random.randint(0, 100)
score2 = random.randint(0, 100)
print(str(score1) + "," + str(score2))

sum = score1 + score2
print("합계 = " + str(sum))

avg = sum // 2
print("평균 = " + str(avg))

cutLine = (score1 > 50 and score2 > 50 ) and avg >= 60
str = ""
if cutLine : str = "합격"
else : str = f"(불합격) score1 = {score1}, score2 = {score2}"
print(str)