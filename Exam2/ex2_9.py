"""
날짜 : 2021/05/13
이름 : 홍길동
내용 : 파이썬 예외처리 연습문제
"""
import math, random

answer = math.ceil(random.random() * 45)
number = 0
count = 0

while True:
    count += 1
    print('-------------------')
    print('answer를 맞춰보세요.')
    number = input('1 ~ 45 사이의 값 입력 : ')

    try:
        # 문자를 숫자로 변환
        number = int(number)
    except:
        print('숫자를 입력하십시오!')
        return

    if number < 0:
        print('음수를 입력 할 수 없습니다.')
        return

    if answer > number:
        print('더 큰수를 입력하세요.')

    elif answer < number:
        print('더 작은 수를 입력하세요.')

    else:
        print('정답 :', answer)
        print('맞추셨습니다!')
        print('시도횟수 : %d회' % count)
    break

print('프로그램 정상종료...')