import speech_recognition as sr
import pyttsx3
import sqlite3

# 음성 인식 초기화
recognizer = sr.Recognizer()

# 음성 출력 초기화
engine = pyttsx3.init()


# 데이터베이스 연결 (SQLite 사용)
def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT
                      )''')
    conn.commit()
    conn.close()


def check_user_credentials(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()


# 음성으로 로그인 정보 입력 받기
def listen_for_credentials():
    with sr.Microphone() as source:
        print("음성을 입력해주세요.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("음성을 텍스트로 변환 중...")
            text = recognizer.recognize_google(audio, language="ko-KR")
            print(f"인식된 텍스트: {text}")
            return text
        except sr.UnknownValueError:
            print("음성을 이해할 수 없습니다.")
        except sr.RequestError:
            print("음성 인식 서비스에 문제가 발생했습니다.")
        return None


# 로그인 프로세스
def login():
    print("로그인 시스템입니다.")
    username = listen_for_credentials()  # 사용자명
    if not username:
        return
    print(f"입력된 사용자명: {username}")

    password = listen_for_credentials()  # 비밀번호
    if not password:
        return
    print(f"입력된 비밀번호: {password}")

    if check_user_credentials(username, password):
        print("로그인 성공!")
        engine.say("로그인에 성공했습니다.")
        engine.runAndWait()
    else:
        print("로그인 실패!")
        engine.say("로그인에 실패했습니다. 다시 시도해주세요.")
        engine.runAndWait()


# 사용자 등록 프로세스
def register():
    print("새로운 사용자 등록 시스템입니다.")
    username = listen_for_credentials()  # 사용자명
    if not username:
        return
    print(f"입력된 사용자명: {username}")

    password = listen_for_credentials()  # 비밀번호
    if not password:
        return
    print(f"입력된 비밀번호: {password}")

    register_user(username, password)
    print("사용자가 등록되었습니다.")
    engine.say("사용자가 등록되었습니다.")
    engine.runAndWait()


# 메인 메뉴
def main():
    create_db()  # 데이터베이스 초기화
    while True:
        print("\n메뉴: 1. 로그인 2. 회원가입 3. 종료")
        choice = input("선택하세요: ")
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
