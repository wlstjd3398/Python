"""
날짜 : 2021/05/13
이름 : 홍길동
내용 : 파이썬 클래스 연습문제
"""

class king:
    def __init__(self, name='태조', year=1392):
        self.name = name
        self.year = year

    def show(self):
        print('----------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':
    king1 = king()
    king2 = king('태종')
    king3 = king('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()