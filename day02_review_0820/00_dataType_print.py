# 데이터 타입 (int, float, string, boolean)
# 데이터 타입확인
# int() -> int 타입으로 변환
# str() -> str 타입으로 변환
# float() -> float 타입으로 변환

number1 = 10
changeNumber_str = str(number1)
print(type(changeNumber_str)) # int -> str

changeNumber_int = int(changeNumber_str) # str -> int
print(type(changeNumber_int))

changeNumber_float =float(changeNumber_str)
print(type(changeNumber_float))


# 출력함수 f {}
name = "David"
age = "27"
mbti = "ENTJ"

print(f"내 이름은 {name}이고, 나이는 {age}, mbti는 {mbti}")

# {값:<자릿수} : 값을 자릿수 만큼 차지,왼쪽 정렬
print(f"나이 : {age:<5}")
# {값:>자릿수} : 값을 자릿수 만큼 차지,오른쪽 정렬
print(f"나이 : {age:>5}")
# {값:^자릿수} : 값을 자릿수 만큼 차지, 가운데 정렬
print(f"나이 : {age:^5}")

# 소숫점 자릿수만큼 반올림
print(f"키:{165.163333:0.1f}") # 소숫점 자릿수만큼 반올림
pi = 3.141592
print(f"pi : {pi:>5.3f}") # 5칸 만큼 오른쪽 정렬하면서, 소숫점은 3자리에서 반올림

print("안녕\n파이썬")
print("안녕\t파이썬")
print("안녕\\파이썬")
print("안녕\"파이썬\"")
print("안녕\'파이썬\'")


