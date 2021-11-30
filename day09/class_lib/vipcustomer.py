#VIPCustomer클래스 정의
from day09.class_lib.customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name) #부모 멤버 상속
        self.agent = agent #추가된 전문 상담원 멤버
        self.cgrade = "VIP" #VIP등급
        self.sale_ratio = 0.1 #구매할인율 10#
        self.bonus_ratio = 0.05 #

    def calc_price(self, price): #부모 매서드 재정의
        price = price - int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self): #부모 정보 상속
        return super().__str__() + "\n전문상담원 ID는 {}입니다".format(self.agent)