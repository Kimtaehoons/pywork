#book테이블 만들기
import sqlite3

def getconn():
    con = sqlite3.connect('./output/sample.db')
    return con

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
    CREATE TABLE book(
        book_no INTEGER PRIMARY KEY AUTOINCREMENT, #PRIMARY KEY와 AUTOINCREMENT 한 세트
        title TEXT NOT NULL,
        publisher TEXT NOT NULL,
        page INTEGER
    )
    """
    #AUTOINCREMENT - 자동 순번(sequence) db브라우저에서 하나의 테이블로 인식
    cur.execute(sql)
    conn.commit()
    print("book테이블 생성")
    conn.close()

#def insert_book():
    #conn = getconn()
    #cur = conn.cursor()
    #sql = "INSERT INTO book (title, publisher, page) VALUES ('웹 표준의 정석', '고경희', '600')" #book_no는 자동 순번 입력되게끔 했으므로 제외하고 이 제외되면서 employee 뒤에 칼럼명 명시해서 맞춰준다
    #cur.execute(sql)
    #conn.commit()
    #conn.close()

#동적 입력
def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO book (title, publisher, page) VALUES (?, ?, ?)" #book_no는 자동 순번 입력되게끔 했으므로 제외하고 이 제외되면서 employee 뒤에 칼럼명 명시해서 맞춰준다
    cur.execute(sql, ('웹 표준의 정석', '고경희', 600))
    conn.commit()
    conn.close()

def select_book(): #db브라우저에서 확인 안 하고자
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM book"
    cur.execute(sql)
    rs = cur.fetchall()
    #print(rs)
    for i in rs:
        print(i)
    conn.close() #commit이 필요없음

def select_one(): ##현재 오류##
    conn = getconn()
    cur = conn.cursor
    sql = "SELECT * FROM book WHERE book_no=?" #책 번호로 검색
    cur.execute(sql, (1, ))
    rs = cur.fetchone()
    print(rs)
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE book SET page=? WHERE book_no=?" #page=300->350 변경
    cur.execute(sql, (350, 3)) #page, book_no순으로 작성
    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()
    #sql = "DELETE FROM book WHERE book_no=?"  #book_no=1인 책 삭제
    sql = "DELETE FROM book" #전체 자료 삭제(번호가 살아있다 그래서 번호를 초기화 시키려면 drop을 써야한다)
    cur.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #create_table()
    #insert_book()
    #select_one()
    #update_book()
    #delete_book()
    #select_book()