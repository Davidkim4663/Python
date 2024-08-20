'''
[문제]
    0에서 100사이의 랜덤 숫자를 시험 점수로 저장한다.
    시험점수에 해당하는 학점을 출력하시오.
    아래는 점수표이다.
    100~91 이면 A학점,
    90~81  이면 B학점,
    80이하는 "재시험"

    단, 만점이거나, A학점과 B학점의 일의 자리가 8점이상이면 + 기호를 추가하시오.
    [예]
        100 => A+
        88 ==> B+
        82 ==> B
        23 ==> 재시험
'''
import random
score = 97
print("score = " + str(score))
# 일의자리 8

unit_8 = score % 10


# scoreScope
score_perfect = score == 100
score_a = 99 >= score >= 91  # a
score_b = 90 >= score >= 81  # b
score_fail = score < 80 # fail
score_alpha_a = score_a and unit_8 >= 8
score_alpha_b = score_b and unit_8 >= 8

score_str = ""
if score_perfect : score_str = f"{score} => A+"
elif score_a : score_str = f"{score} => A"
if score_alpha_a : score_str = f"{score} => A+"
elif score_b : score_str =  f"{score} => B"
if score_alpha_b : score_str = f"{score} => B+"
elif score_fail : score_str =  f"{score} =>재시험"
print(score_str)
    
  