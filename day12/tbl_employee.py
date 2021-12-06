import sqlite3

#중복되는 부분 정리
def getconn():
    con = sqlite3.connect("c:/pydb/mydb.db") #다른 곳에 있는 것을 네트워크 연결을 통해 자료를 가져옴, mydb에 db가 없어도 여기서 만들어짐)
    return con

#전체 자료 검색
def select_emp():
    conn = getconn() #db 연결 객체 생성
    cur = conn.cursor() #db 작업 개체
    sql = "SELECT * FROM employee ORDER BY emp_id" #db 검색
    cur.execute(sql) #검색 실행
    rs = cur.fetchall() #db 저장된 모든 데이터 가져오기
    #print(rs) #전체 출력
    for i in rs: #각각 출력
        print(i)
    conn.close() #db 연결 종료

#자료 추가
def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    #데이터 입력방법 1. 직접 입력
    #sql = "INSERT INTO employee VALUES ('e1006', '박찬호', 40, 100000)" #db 추가
    #cur.execute(sql)
    #conn.commit()  # 변경 사항이 생겼을 때 필수
    #conn.close()

    #데이터 입력방법 2. 동적 입력('?' 사용)
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"  # db 추가
    cur.execute(sql, ('e1008', '박지성', 19, 70000))
    conn.commit() #변경 사항이 생겼을 때 필수
    conn.close()

    #데이터 입력방법 3. 리스트로 입력(추후)

#특정 자료 검색
#방법 1.
#def select_one():
    #conn = getconn()
    #cur = conn.cursor()
    #sql = "SELECT emp_id, name FROM employee WHERE salary = 70000"
    #cur.execute(sql)
    #rs = cur.fetchone() #1명의 자료 반환(여러 명의 자료값이 나올 때는 반복문을 써서)
    #print(rs)
    #conn.close()

#방법 2.
def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT emp_id, name FROM employee WHERE emp_id=?"
    cur.execute(sql, ('e1008', )) #튜플 구조는 콤마를 찍어야 함
    rs = cur.fetchone() #1명의 자료 반환(여러 명의 자료값이 나올 때는 반복문을 써서)
    print(rs)
    conn.close()

#자료 수정
def update_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age=? WHERE emp_id=?"
    cur.execute(sql, (35, 'e1004'))
    conn.commit()
    conn.close()

#자료 삭제
def delete_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name=?"
    cur.execute(sql, ('안산',))
    conn.commit()
    conn.close()

if __name__ == "__main__": #이 모듈을 다른 파일에서 활용할 때 출력 파일에서 이 내용이 나오지 않게끔 하기 위함
    #insert_emp() #처음 추가 할 때 열어두고, 다음 작업 시 닫아둔다(계속 열어두고 실행하면 계속 추가되기 때문)
    #select_one() #방법 2의 호출
    update_emp()
    #delete_emp()
    select_emp()