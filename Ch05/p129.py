# (1) 튜플형 가변인수
def Func1(name, *names):
    print(name) # 실인수 : 홍길동
    print(names)    # 실인수 : ('이순신', '유관순')

Func1("홍길동", "이순신", "유관순")

# statistics 모듈 import
from statistics import mean, variance, stdev

# (2) 통계량 구하는 함수
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return  variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'

# statis 함수 호출
print('avg=', statis('avg', 1, 2, 3, 4, 5))
print('var=', statis('var', 1, 2, 3, 4, 5))
print('std=', statis('std', 1, 2, 3, 4, 5))

# (3) 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

# emp_func 함수 호출
emp_func('홍길동', 35, addr='서울시', height=175, weight=65)


