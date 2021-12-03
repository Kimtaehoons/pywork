import sqlite3
#데이터 조회
def select_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db") #db 연결 객체 생성
    cur = conn.cursor() #db 작업 개체
    sql = "SELECT * FROM employee" #db 검색
    cur.execute(sql) #검색 실행
    rs = cur.fetchall() #db 저장된 모든 데이터 가져오기
    #print(rs) #전체 출력
    for i in rs: #각각 출력
        print(i)
    conn.close() #db 연결 종료
#데이터 추가
def insert_emp():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e1002', '손흥민', 30, 50000)" #db 추가
    cur.execute(sql)
    conn.commit() #변경 사항이 생겼을 때 필수
    conn.close()

#insert_emp() #처음 추가 할 때 열어두고, 다음 작업 시 닫아둔다
select_emp()