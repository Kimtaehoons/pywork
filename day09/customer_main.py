from day09.class_lib.customer import Customer
from day09.class_lib.goldcustomer import GoldCustomer
from day09.class_lib.vipcustomer import VIPCustomer

c = Customer(101, "놀부") #Customer객체 생성(from day09.class_lib.customer import Customer)
g = GoldCustomer(201, "흥부") #GoldCustomer객체 생성(from day09.class_lib.goldcustomer import GoldCustomer)
v = VIPCustomer(301, "심청", 1004) #VIPCustomer객체 생성(from day09.class_lib.vipcustomer import VIPCustomer)
#효율적으로 관리하려면 리스트 안으로 넣어야 한다(customer_list.py참고)

#제품 구매
cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(10000)

#제품 지불 비용 출력
print(c.getname() + "님의 지불비용은" + str(cost_c) + "원 입니다") #c.name을 바로 쓰지 말고 정보은닉을 위해 getname으로 써준다
print(g.getname() + "님의 지불비용은" + str(cost_g) + "원 입니다")
print(v.getname() + "님의 지불비용은" + str(cost_v) + "원 입니다")

#객체 정보 확인
print(c)
print(g)
print(v)