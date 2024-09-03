"""
[문제1] 딕셔너리 생성 및 접근
[ 지문 ]  학생의 이름과 나이를 포함하는 딕셔너리 students를 생성하세요. 아래  조건에 따라 코드를 작성하시오,
[ 샘플 코드 ]
"""

students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 21
}
print("student : ", students)
print()
# [ 조건 ]
# 1. students 딕셔너리에 "David"라는 키를 추가하고, 그의 나이를 23으로 설정하세요.
students["David"] = 23
print("student(David insert) : ", students)
# 2. "Alice"의 나이를 21로 업데이트하세요.
students['Alice'] = 21
print("student(Alice update) : ", students)

# 3. students 딕셔너리에서 "Bob"의 나이를 출력하세요.
BobAge = students['Bob']
print("BobAge = ", BobAge)
print()
# [문제2] 딕셔너리 값 합산
# [ 지문 ]  딕셔너리 sales는 각 제품과 그 제품의 판매량을 나타냅니다. 아래  조건에 따라 코드를 작성하시오,
# [ 샘플 코드 ]
# [ 조건 ]
# 1. 모든 제품의 판매량의 합을 계산하세요.
sales = {
    "Laptop": 1500,
    "Smartphone": 1200,
    "Tablet": 800
}
sales_laptop = sales['Laptop']
print("sales_laptop = ", sales_laptop)

sales_Smartphone = sales['Smartphone']
print("Smartphone = ", sales_Smartphone)

sales_Tablet = sales['Tablet']
print("sales_Tablet = ", sales_Tablet)

sales_total = sales_laptop + sales_Smartphone + sales_Tablet
print("total = ",sales_total)

sales['total_price'] = sales_total
print(sales)


# [문제3] 딕셔너리에서 키와 값 추출
# [ 지문 ]  딕셔너리 person이 다음과 같이 주어졌다고 가정합니다 .
# 아래  조건에 따라 코드를 작성하시오,
# [ 샘플 코드]
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# [ 조건 ]
# 1. person 딕셔너리의 모든 키를 리스트로 출력하세요.
list_person_key = list(person.keys())
print("list_person_key = ", list_person_key)

# 2. person 딕셔너리의 모든 값을 리스트로 출력하세요.
list_person_value = list(person.values())
print("list_person_value = ", list_person_value)

# [문제4] 딕셔너리의 키 존재 여부 확인
# [ 지문 ]  딕셔너리 contacts는 연락처 정보를 저장합니다.

# 아래  조건에 따라 코드를 작성하시오,
# [ 샘플 코드 ]

contacts = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}
# 1. "Dave"라는 키가 contacts 딕셔너리에 존재하는지 확인하고 결과를 출력하세요.
checkingDave = 'Dave' in contacts
print("checkingDave = ", checkingDave)

# 2. "Bob"이라는 키가 contacts 딕셔너리에 존재하는지 확인하고 결과를 출력하세요.
checkingBob = 'Bob' in contacts
print("checkingBob = ", checkingBob)

# [문제5] 중첩 딕셔너리 처리
# [ 지문 ]  다음과 같은 중첩 딕셔너리 company가 있습니다. 아래  조건에 따라 코드를 작성하시오,
# [ 조건 ]
# [ 샘플 코드 ]
company = {
    "HR": {
        "employees": ["John", "Sarah"],
        "budget": 50000
    },
    "IT": {
        "employees": ["Mike", "Anna"],
        "budget": 100000
    }
}
print()
# [ 조건 ]
# 1. company 딕셔너리에서 "IT" 부서의 budget 값을 출력하세요.
printBudget = company['IT']['budget']
print("printBudget" , printBudget)

# 2. "HR" 부서의 employees 리스트에 "Emma"를 추가하세요.
company['HR']['employees'] = 'Emma'
print("company = ", company)

# 이중 딕션 추가 및 접근방법에 대해 궁금합니다.

# 3. 전체 부서의 budget 합계를 계산하세요.
