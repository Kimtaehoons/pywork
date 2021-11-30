#Converter클래스 정의
#온도 변환기 : 화씨온도(F) = 섭씨온도(C) * 1.8 + 32(섭씨를 화씨 온도로)
from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter): #부모(ScaleConverter) 상속 받음
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor) #부모 거('C', 'F', 1.8)
        self.offset = offset #자식 거(32)

    def convert(self, value): #부모 메서드 재정의
        return self.factor * value + self.offset #온도 변환기 식에 따른(단위1 값 X 수) + 단위2 값

conv = Converter('C', 'F', 1.8, 32)
print("Converting 20C")
print(str(conv.convert(21)) + conv.units_to)
print("%.2f" % conv.convert(21))