"""
날짜 : 2022/04/29
이름 : 김철학
내용 : 파이썬 내장함수 교재 p118
"""

import math # 모듈 선언
import random   # 모듈 선언
import time # 모듈 선언

# 수학관련
r1 = abs(-5)    # abs는 절대값 나타나게해줌
print('r1 :', r1)

r2 = math.ceil(1.2) # 모듈선언하고 ceil은 천장함수, 상위로 올림
r3 = math.ceil(1.8)
print('r2 :', r2)
print('r3 :', r3)

r4 = math.floor(1.2)    # 모듈선언하고 floor는 바닥함수, 하위로 내림
r5 = math.floor(1.8)
print('r4 :', r4)
print('r5 :', r5)

r6 = round(1.2) # round는 반올림
r7 = round(1.8)
print('r6 :', r6)
print('r7 :', r7)

# 제곱근
r8 = math.sqrt(4)
r9 = math.sqrt(9)
print('r8 :', r8)
print('r9 :', r9)

# random 모듈선언하고 0 ~ 1사이의 실수 무작위 표현
num1 = random.random()
print('num1 :', num1)

num2 = num1 * 10
print('num2 :', num2)   # 0 ~ 10 사이에 실수 무작위 표현

num3 = math.ceil(num2)
print('num3 :', num3)   # 1 ~ 10 사이에 정수 무작위 표현

num4 = math.ceil(random.random() * 10)
print('num4 :', num4)   # 1 ~ 10 사이에 정수 num1, num2, num3 중첩확인

# 날짜, 시간
t1 = time.time()
print('t1 :', t1)   # unix time으로 나옴 1970년 1월 1일부터 순서대로 표현된것

t2 = time.ctime()
print('t2 :', t2)    # 변환된 Unix time


now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' % (year, month, date))
print('%s시 %s분 %s초' % (hour, min, sec))

