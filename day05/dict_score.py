#총 3명의 학생의 성적 합계 및 평균
student = [
    {'name':"김하나", 'kor':80, 'math':70, 'eng':90}, #한 명의 세 과목의 점수
    {'name':"이하나", 'kor':60, 'math':50, 'eng':40},
    {'name':"박하나", 'kor':90, 'math':90, 'eng':100}
]

#개인별 총점과 평균
print("  이름    총점    평균")
for s in student: #student안에 있는 요소(출력방식의 차이 : 딕셔너리일수도, 리스트일수도)
    sum_v = s['kor'] + s['math'] + s['eng'] #인덱스로 값 찾기
    avg = sum_v / 3
    print("%s   %d    %.1f" % (s['name'], sum_v, avg)) #대응 서식 문자 - 정수 : %d, 실수 %f, 문자열 : %s

#과목별 총점과 평균
sum_subj = [0, 0, 0]
avg_subj = [0.0, 0.0, 0.0]

for s in student:
    sum_subj[0] += s['kor']
    sum_subj[1] += s['math']
    sum_subj[2] += s['eng']

avg_subj[0] = sum_subj[0] / 3
avg_subj[1] = sum_subj[1] / 3
avg_subj[2] = sum_subj[2] / 3

print("국어 합계 : %d점" % sum_subj[0])
print("수학 합계 : %d점" % sum_subj[1])
print("영어 합계 : %d점" % sum_subj[2])
print("국어 평균 : %.1f점" % avg_subj[0])
print("수학 평균 : %.1f점" % avg_subj[1])
print("영어 평균 : %.1f점" % avg_subj[2])