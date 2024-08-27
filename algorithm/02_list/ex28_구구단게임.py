'''
	[문제]
		a와 b의 각 자리의 곱을 total의 각 자리에 저장 후 출력하시오.
  		단 op 의 값이 0이면 양수로 저장하고,
		1이면 음수로 저장하시오.

	[예시]
		a = 3 , b = 5 , op = 0 이므로 양수로 저장 total = [15]
		a = 4 , b = 3 , op = 1 이므로 음수로 저장 total = [15, -12]
		a = 2 , b = 1 , op = 0 이므로 양수로 저장 total = [15, -12, 2]
		a = 8 , b = 7 , op = 0 이므로 양수로 저장 total = [15, -12, 2, 56]
		a = 8 , b = 7 , op = 1 이므로 음수로 저장 total = [15, -12, 2, 56, -18]
'''
a  = [3, 4, 2, 8, 6]
b  = [5, 3, 1, 7, 3]
op = [0, 1, 0, 0, 1]
gugudan_rs = 0

total = []
for i in range(len(a)) :
    gugudan_rs = a[i] * b[i]
    checkPlus = op[i] == 0 # op의 값이 양수일 때
    checkMinus = op[i] == 1 # op의 값이 음수일 때
    if checkPlus :
        total.append(gugudan_rs)
    elif checkMinus :
        total.append(-gugudan_rs)
    print(f"a = {a[i]}, b = {b[i]}, op = {op[i]} 이므로 " "total = ", total)

print("total = ", total)

