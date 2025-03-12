import sqlite3

# 데이터베이스 경로 설정 (JDBC URL에서 jdbc:sqlite: 부분 제외)
db_path = r"C:\voice\users.db"

# SQLite 데이터베이스 연결
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 예시: users 테이블의 모든 데이터 조회
cursor.execute('SELECT * FROM users;')
rows = cursor.fetchall()

#삭제할 username, password설정
username_to_delete = "today's weather"
password_to_delete = "passwort"

# DELETE 쿼리: username과 password가 일치하는 레코드 삭제
cursor.execute('''
    DELETE FROM users 
    WHERE username = ? AND password = ?;
''', (username_to_delete, password_to_delete))

# 변경 사항 커밋
conn.commit()

cursor.execute('SELECT * FROM users;')
rows = cursor.fetchall()
if not rows:
    print("Empty")
else:
    print("-----Content------")
    # 데이터 출력
    for row in rows:
        print(row)
# 연결 종료
conn.close()
