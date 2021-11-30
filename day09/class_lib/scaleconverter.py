#ScaleConverter클래스 정의
#inch를 mm로 변환하기 : 1inch -> 25mm
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from #단위1(inch) 값
        self.units_to = units_to #단위2(변환할 단위, mm) 값
        self.factor = factor #변환요소(값, 25)

    def convert(self, value): #변환 계산 함수
        return self.factor * value #변환 값 X 숫자

if __name__ == "__main__":
    sc = ScaleConverter("inches", "mm", 25) #생성자 함수(def__init__)의 괄호 안 순서대로
    print("Converting 10 inches")
    print(str(sc.convert(10)) + sc.units_to)