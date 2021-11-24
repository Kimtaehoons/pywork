#배송비 계산하기
#사용자 함수 정의(get_price)
def get_price(unit_price, quantity):
    delivery_fee = 2500
    price = unit_price * quantity
#상품 가격이 20000원 미만이면 배송비(2500원) 포함하고 아니면 배송비 미포함
    if price < 20000:
        price += delivery_fee
        return price #if가 한 번 들어가면 거기에 따른 별도의 return을 해줘야한다
    else:
        return price #일반적으로는 else의 경우라고 생각한다면

price1 = get_price(15000,2)
price2 = get_price(5000, 3)

print("상품1의 가격은 " + str(price1) + "원 입니다")
print("상품2의 가격은 " + format(price2, ',d') + "원 입니다") #천 단위 구분 기호
