'''
    [문제]
        omr 리스트의 값들은 이번 시험 정답이다.
        a는 철수의 답안지이다. 랜덤숫자(1~5) 열 개를 a에 추가 후,
        정답과 비교해서 철수의 점수를 출력.
        한 문제당 10점이다.
    [예시]
        omr  = [4, 3, 1, 5, 3, 2, 1, 4, 5, 3]
        철수 = [5, 2, 5, 5, 2, 1, 4, 4, 4, 1]
        성적 = 20
'''
import random

omr = [4,3,1,5,3,2,1,4,5,3]
myAnswer =[]
print("omr = ", omr)

cnt = 0
myAnswer_o = 0

for i in range(10) :
    myExam = random.randint(1, 5)
    myAnswer.append(myExam)
print("my Answer = ", myAnswer)

for i in range(len(omr)) :
    checkingAnswer = omr[i] == myAnswer[i]
    if checkingAnswer :
        myAnswer_o += 10 # 답안지와 내 답안지가 같으면 + 10점
        cnt += 1

print("철수의 점수 = ", myAnswer_o,"\n맞춘 문제 = ",cnt)