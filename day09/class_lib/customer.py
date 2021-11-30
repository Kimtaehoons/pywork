#Customer클래스
class Customer:
    def __init__(self, cid, name):
        self.cid = cid #고객 ID
        self.name = name # 고객 성명
        self.cgrade = "SILVER" #고객 등급
        self.bonus_point = 0 #보너스 포인트
        self.bonus_ratio = 0.01 #보너스 적립률 : 1%

    def getname(self):
        return self.name

    def calc_price(self, price):
        self.bonus_point += int(price * self.bonus_ratio) #포인트는 가격 x 보너스 적립률로 계산하고 정수형으로 변경
        return price

    def __str__(self):
        return "{}님의 등급은 {}이고, 보너스 포인트는 {}점 입니다"\
            .format(self.name, self.cgrade, self.bonus_point)