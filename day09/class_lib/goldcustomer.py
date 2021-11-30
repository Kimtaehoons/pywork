#GoldCustomer클래스 정의(Customer 상속 받음, 부모의 속성 중에 달라진 것들만 써준다)
from day09.class_lib.customer import Customer

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name) #부모 멤버 상속
        self.cgrade = "GOLD" #자기 멤버
        self.sale_ratio = 0.1 #자기 멤버(구매 할인율 10%)
        self.bonus_ratio = 0.02 #자기 멤버(보너스 적립률 2% 변경됨)

    def calc_price(self, price): #부모 메서드 재정의
        price = price - int(price * self.sale_ratio) #기존 가격에서 자식 멤버가 추가됨에 따라 변동된 계산식 정의(할인된 가격 = 가격 - (가격 x 구매 할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price