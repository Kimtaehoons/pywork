#주요 내장 함수
#all() - 반복 자료(리스트나 튜플)에 0이 하나라도 있으면 false(의미상 and와 같음)
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

#any() - 반복 자료(리스트나 튜플)에 모두 0일 때만 false
print(any([1, 2, 3, 0]))

#eval() - 문자열 표현 -> 숫자로 표현
print(eval("1+2"))

#list() - 자료를 리스트로 반환
print(list('python'))

#abs() - 절대값
print(abs(-10))

#round() - 반올림
print(round(4.7))
print(round(4.51))
print(round(4.4))

#sum() - 합계
print(sum([1, 2, 3, 4]))

#min() - 최소값
print(min([1, 2, 3, 4]))

#pow() - 거듭제곱
print(pow(2, 4))