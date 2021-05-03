"""
날짜 : 2021/04/28
이름 : 김철학
내용 : 파이썬 함수 Function 실습 교재 p114

함수(Function)
 - 프로그래밍에서 일련의 로직 단위를 모듈로 만든것
 - 함수는 정의 ,호출로 이루어진다
"""

# 함수정의
def f(x):
    y = 2 * x + 3
    return y

# 함수호출
r1 = f(1)
r2 = f(2)
r3 = f(3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 함수유형1 - 매개변수 o 리턴값 o
def type1(x, y):
    z = x + y
    return z

rs1 = type1(1, 2)   # 1, 2는 인자값이라고 부른다
rs2 = type1(2, 3)

print('rs1 :', rs1)
print('rs2 :', rs2)


# 함수유형2 - 매개변수 o 리턴값 x
def type2(items):
    total = 0

    for item in items:
        total += item

    print('items 합 :', total)

type2([1, 2, 3, 4, 5])
type2((2, 4, 6, 8, 10))


# 함수유형3 - 매개변수 x 리턴값 o
def type3():
    total = 0

    for i in range(11):
        total += i

    return total

result = type3()
print('result :', result)


# 함수유형4 - 매개변수 x 리턴값 x
def type4():
    print('type3 result :', type3())

type4()


# 확인문제
def gugudan(num):
    print(num, '단')
    print('{} x 1 = {}'.format(num, num*1))
    print('{} x 2 = {}'.format(num, num*2))
    print('{} x 3 = {}'.format(num, num*3))
    print('{} x 4 = {}'.format(num, num*4))
    print('{} x 5 = {}'.format(num, num*5))
    print('{} x 6 = {}'.format(num, num*6))
    print('{} x 7 = {}'.format(num, num*7))
    print('{} x 8 = {}'.format(num, num*8))
    print('{} x 9 = {}'.format(num, num*9))

# 같은 식이나 줄인 식이 좋음
def gugudan(num):
    print(num, '단')
    for i in range(1, 10):
        print('{} x {} = {}'.format(num, i, num*i))


gugudan(2)
gugudan(3)
gugudan(7)