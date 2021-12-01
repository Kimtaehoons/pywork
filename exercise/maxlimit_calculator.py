from exercise.calculator import Calculator

class MaxLimitCalculator(Calculator):

    def add(self, val): #부모(calculator) def add(self, val)함수에서 100 이상의 값에 대한 처리가 필요하므로 부모 매서드(함수) 재정의가 필요하다
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)