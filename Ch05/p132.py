# (1) 지역변수 예
x = 50  # 전역변수
def local_func(x) :
    x += 50 # 지역변수 -> 종료 시점 소멸
local_func(x)
print('x=', x)

# (2) 전역변수 예
def global_func():
    global x    # x+50 = 100
    x += 50
global_func()
print('x=', x)