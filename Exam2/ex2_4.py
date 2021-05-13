"""
날짜 : 2021/05/13
이름 : 홍길동
내용 : 파이썬 로또 번호 생성 연습문제
"""

import math, random

def lotto():

    lotto_set = set()   # 주머니생성

    while True:
        num = math.ceil(random.random() * 45)

        lotto_set.add(num)

        if len(lotto_set) == 6: # 주머니안에 6개
            break
    return list(lotto_set)

if __name__ == '__main__':

    for i in range(5):  # 5번 반복
        # 로또 번호 생성
        lotto_nums = lotto()

        # 로또 정렬
        lotto_nums.sort()

        # 번호 출력
        print(lotto_nums)