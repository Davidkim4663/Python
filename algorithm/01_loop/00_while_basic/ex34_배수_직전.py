'''
[문제]
    세 자릿수의 28의 배수 중에서 가장 큰 수를 출력하시오.
[정답]
    980
'''
'''
[설명]
    a 변수 하나로 숫자를 저장하게 되면 1000 이상을 체크할 수 없기 때문에 
    number라는 변수를 써서 1000 이상이 되기 직전의 값을 저장해야한다. 
'''
max = 0
i = 1
endNum = 1000
while i <= endNum :
    checkingMultiple = i % 28 == 0
    if checkingMultiple :
        max = i
    i += 1
print("max = ", max)
