#만든 모듈 새 파일에서 불러오기
from day09.class_lib.supersonic_airplane import SuperSonicAirPlane

sa = SuperSonicAirPlane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirPlane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirPlane.NORMAL
sa.fly()
sa.land()