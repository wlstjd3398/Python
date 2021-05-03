from Ch06.sub1.Account import Account

# 클래스 정의
class StockAccount(Account):

    def __init__(self, bank, id, name, money, stock, amount, price):
        # 부모클래스 생성자 실행
        super().__init__(bank, id, name, money)
        # __init__링크 누르는거는 ctrl 누른채로 클릭
        self.stock = stock
        self.amount = amount
        self.price = price

    def buy(self, amount, price):
        print('{}를 {}개 {}가격에 구매함'.format(self.stock, amount, price))

    def sell(self, amount, price):
        print('{}를 {}개 {}가격에 판매함'.format(self.stock, amount, price))

    def show(self):
        super().show()
        print('주식종목 : ', self.stock)
        print('주식수량 : ', self.amount)
        print('주식가격 : ', self.price)