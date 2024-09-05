"""

 함수 :
  함수 : 클래스 밖에서 정의된 함수
  메소드 : 클래스 안에서 정의된 함수

 메소드 :
        - 클래스 안에서 선언되는 함수
        - 객체의 행동

"""


# ex) 학생설계, (변수/자료) 이름, (자료)도시락 (행동/실행)밥먹기
class Student:
    # 생성자
    def __init__(self, name):
        self.name = name

    def lunchGive(self, lunchbox):
        print(f'{self.name}에게 {lunchbox}의 도시락 대입')
        self.lunchbox = lunchbox
        
    def lunchEat(self):
        print(f'{self.name}에게 {self.lunchbox}를 먹습니다')



#  유재석
s1 = Student('유재석')
s2 = Student('강호동')

# 도시락 주는 행위

s1.lunchGive('도시락')
s1.lunchEat()
