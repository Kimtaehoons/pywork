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
first_ul = soup.find('ul', attrs={'class':'item'}) #attrs=속성을 의미하고 딕셔너리로 찾음. 왼쪽에 쓴 코딩이 더 많이 쓰인다. ex1의 first_ul.find('li')와 같은 의미
all_li = first_ul.find_all('li') #find_all()로 찾은 모든 값을 리스트로 반환

print(all_li)
print(all_li[1])
print(all_li[1].text) #정확히 찾아가서 출력
