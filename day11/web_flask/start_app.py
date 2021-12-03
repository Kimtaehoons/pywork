#웹 서버 만들기
from flask import Flask, render_template, request

app = Flask(__name__) #Flask객체 app 생성

@app.route('/') #'/' - 루트 경로, ip - 127.0.0.1(host):5000(port)

#'/'페이지별로 만들기
#index 페이지
def index():
    #return "<h1>Hello~ Flask!!</h1>" #문자열을 index 페이지(루트 경로로)에 전송
    return render_template('index.html') #html파일로 index 페이지(루트 경로로)로 전송

#로그인 페이지
#@app.route('/login/') #주소의 경로 이름과(login)과 함수 이름(login)을 동일하게 설정해야함
#def login():
#    return "<h1>로그인 페이지입니다</h1>"

#회원가입 페이지
@app.route('/register/', methods=['GET', 'POST']) #변수(매개인자 추가)
def register():
    #return "<h1>회원가입 페이지입니다</h1>"
    if request.method == 'POST': #회원가입 내용은 보완이 필요하므로 POST방식, 공개된 페이지 내에서 보완이 필요한 내용은 별도로 다른 창으로 나타나게 된다
        id = request.form['id'] #html의 id를 가져옴
        pwd = request.form['passwd'] #html의 passwd를 가져옴
        name = request.form['name']
        return render_template('member_info.html', id=id, pwd=pwd, name=name) #html의 가입 버튼을 누르면, 폼을 통해 받은 내용(id, pwd, name)이 출력됨
    else: #주소 공개(GET방식), 우선 입력 창이 전체적으로 공개되고
        return render_template('register.html')

#게시판 페이지
#@app.route('/board/')
#def board():
#    return "<h1>게시판 페이지입니다</h1>"

@app.route('/loop_index/') #GET방식만 있을 때는 method 생략 가능
def get_loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loop_index.html', items=items)

@app.route('/even_odd/', methods=['GET', 'POST'])
def even_odd():
    if request.method == "POST":
        try:
            #데이터 수집
            num = int(request.form['num']) #전달 받은 데이터는 문자형태이므로 숫자형태로 바꿔줘야 계산됨
        except ValueError:
            error_message = "숫자를 입력해주세요"
            return render_template('even_odd.html', error_message=error_message) #error_message를 html로 보내면 html에서 받아서 출력까지 마침
        else:
            #데이터 처리
            if num % 2 == 0:
                result = "짝수입니다"
            else:
                result = "홀수입니다"
            return render_template('calc_result.html', num=num, result=result) #if안의 계산 결과값을 새로운 페이지로 result를 넘겨주고 출력함
    else: #GET인 경우
        return render_template('even_odd.html') #html파일 화면에 띄우기

app.run(debug = True) #'debug = True' - 서비스 하기 전 개발 모드