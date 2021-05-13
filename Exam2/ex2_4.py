"""
날짜 : 2021/05/13
이름 : 홍길동
내용 : 파이썬 로또 번호 생성 연습문제
"""

import math, random

def lotto():

    lotto_set = set()

    while True:
        num = math.ceil(random.random() * 45)



        if len(lotto_set) == 6:
            break
    return list(lotto_set)

if __name__ == '__main__':

    for i in range(5):
        # 로또 번호 생성
        lotto_nums = lotto()

        # 로또 정렬
        lotto_nums.sort()

        # 번호 출력
        print(lotto_nums)