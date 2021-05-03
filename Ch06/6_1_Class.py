"""
날짜 : 2022/04/29
이름 : 김철학
내용 : 파이썬  객체지향프로그래밍 Object는 class로 지정 = instance 교재 p148
설계도로 class - instance1, instance2, intance3 여러 차들을 만듬
"""

from Ch06.sub1.Account import Account   # 모듈을 따로 빼야함

from Ch06.sub1.Computer import Computer

# 객체생성(kb wr 참조변수라고도함)
kb = Account('국민은행', '101-12-1010', '김유신', 10000)
kb.deposit(40000)
kb.withdraw(7000)
kb.show()

wr = Account('국민은행', '101-12-1010', '김유신', 30000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()



# 객체생성(samsung, lg)
samsung = Computer('삼성', 'Intel i7', '16GB', '1TB')
imac = Computer('애플', 'Intel i7', '32GB', '1TB')

samsung.info()
imac.info()

