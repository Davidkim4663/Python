'''
    [문제]
        number_list는 학생 다섯 명의 번호이다.
        score_list는 위 학생들의 수학 점수이다.
        60점 이상은 합격이다.
        [조건1] 합격생들의 번호와 점수 출력.
        [조건2] 전체 학생들의 총점과 평균을 출력.
        [조건3] 합격생들이 몇 명인지를 출력.
'''
number_list = [1001, 1002, 1003, 1004, 1005]
score_list  = [  10,   32,   65,   90,   89]
print("학생번호 : ", number_list)
print("학생점수 : ", score_list)

cnt = 0
sum = 0 # 총점
avg = 0 # 평균

print()
print("========================================")
for i in range(len(number_list)) :
    cutLine = score_list[i] >= 60
    if cutLine :
        print("합격생 번호 = ", number_list[i],", 합격생 점수 = ", score_list[i])
        cnt += 1
    sum += score_list[i]
avg = sum / len(number_list)
print("========================================")
print()
print("전체 학생의 총점 = ", sum)
print("전체 학생의 평균 = ", avg)
print(f"전체 학생 중 합격자 수는 = {cnt}명 ")

