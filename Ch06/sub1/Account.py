# 클래스 정의
class Account:  # class 는 바로 뒤 대문자로 시작함
    # 속성
    def __init__(self, bank, id, name, money):  # --로 시작하는것은 특수함수, init은 생성자, self는 class의 멤버
        self.__bank = bank
        self.__id = id
        self.__name = name
        self.__money = money


    # 기능
    def deposit(self, money):   # 입금
        self.__money += money

    def withdraw(self, money):  # 출금
        self.__money -= money

    def show(self): # 잔액을 양식에 따라 표현
        print('-------------------')
        print('은행명 :', self.__bank)
        print('계좌번호 :', self.__id)
        print('입금주 :', self.__name)
        print('현재잔액 :', self.__money)