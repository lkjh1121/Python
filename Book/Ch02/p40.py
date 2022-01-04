"""
날짜 : 2022/01/03
이름 : 김재현
내용 : 파이썬 operator 실습
"""
num1 = 100 # 피연산자1
num2 = 20  # 피연산자2


# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기 비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2 값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2 값이 크거나 같은지 비교
print(bool_result)

# 두 관계식 같은지 판다
log_result = num1 >= 50 and num2 <=10
print(log_result)

# 두 관계식 중 하나라도 같은지 판다
log_result = num1 >= 50 or num2 <=10
print(log_result)

log_result = num1 >= 50 # 관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)