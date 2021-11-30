#SuperSonicAirPlane클래스 정의
from day09.class_lib.airplane import AirPlane

class SuperSonicAirPlane(AirPlane):
    NORMAL = 1 #클래스 상수(대문자)
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL #멤버 fly_mode

    def fly(self): #부모 fly(일반 비행)를 자식 거(초음속과 일반)로 재정의
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC: #산술연산자로 true, false값 반환
            print("비행기가 초음속으로 비행합니다")
        else: #fly_mode == NOMAL
            super().fly()