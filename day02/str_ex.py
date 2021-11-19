#홑따옴표, 쌍따옴표 감싸서 문자열을 표기
say = "'힘내세요!!' 라고 말했습니다"
print(say)

#여러줄 출력하기(쌍따나 홑따로 변수부분 제외하고 감싸준다)
print('='*50)
song1 = '''
동해물과 백두산이\n마르고 닳도록
하느님이 보우하사\n우리나라 만세

남산 위에 저 소나무\n철갑을 두른 듯
바람서리 불변함은\n우리 기상일세
'''
print(song1)
print('='*50)

#이스케이프 문자(\t(탭기능) - 문자 간격, \n - 줄바꿈)
table = """
이름\t나이\t지역
김화성\t21\t화성
"""
print(table)
head = 'python'
tail = ' is fun!'
print(head + tail)
print(head * 2)
