from bs4 import BeautifulSoup #bs4 모듈에 있는 BeautifulSoup클래스를 쓰겠다
html_str = """ 
<html>
    <body>
        <ul class='item'>
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ul>
        <ul class='lang'>
            <li>Python</li>
            <li>java</li>
            <li>C#</li>
        </ul>
    </body>
</html>
"""
#""" """은 여러줄의 문자를 감쌀 때 쓰는 기호 

#계층구조에 맞게 순서대로 작성해준다
soup = BeautifulSoup(html_str, "html.parser") #클래스 생성자()안에 매개변수 넣어서 html_str에서 html.parser를 통해
first_ul = soup.find('ul') #soup를 통해서 find()로 처음 나오는 ul태그를 찾는다
print(first_ul) #태그 포함 출력
print(first_ul.text) #태그 제외한 문자열 출력

first_li = first_ul.find('li') #first_ul 객체로 li태그로 접근
print(first_li)