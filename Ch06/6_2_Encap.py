"""
날짜 : 2022/04/30
이름 : 김철학
내용 : 파이썬  캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행', '101-111-1091', '김유신', 30000)
kb.deposit(10000)
kb.withdraw(5000)
# kb.__money -= 1
kb.show()
# 다른방법으로 입출금이 가능하다면 취약점이 되어서 class 쓴다면 캡슐화를 해야함
# 캡슐로 member변수들 ex(bank id name money)를 보호해서 외부참조에서 참조안되게 내부참조에서만 가능하게 보호해야함
# Account.py에서 member들 __붙여서 캡슐화시킨다
# 캡슐화(정보은닉)를 적용해서  취약코드를 예방한다 필수다