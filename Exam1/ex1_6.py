"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 파이썬 연습문제 2.다이아몬드 출력
"""

count = 0

for i in range(1, 10):

    if i <= 5:
        count += 1
    else:
        count -= 1

    for j in range(5-count):
        print(' ', end ='')

        for k in range(count * 2 - 1):
            print('*', end ='')

print()
