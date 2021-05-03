# (1) 문자형 숫자 입력
num = input("숫자입력 : ")
print('num type :', type(num)) # <class 'str'>
print('num = ', num)
print('num = ', num*2)

# (2) 문자형 숫자를 정수형으로 입력
num1 = int(input ("숫자입력 : "))   #str -> int(형변환)
print('num1 = ', num1*2)

# (4) 문자형 숫자를 실수형으로 변환
num2 = float(input("숫자 입력 : ")) #str -> float(형변환)
result = num1 + num2    #실수 = 정수 + 실수
print('result = ', result)
