import librosa
import numpy as np
import pyaudio
import wave
import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity


# FLAC 파일에서 MFCC 특징 추출 함수
def extract_mfcc_features_from_flac(audio_file):
    y, sr = librosa.load(audio_file)

    # 배경 잡음 제거 (Optional)
    y, _ = librosa.effects.trim(y)  # 앞뒤로 불필요한 침묵 제거
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)  # 평균으로 특징 벡터 추출
    return mfcc_mean


# 사용자 모델 저장 함수
def save_user_model(username, audio_file):
    features = extract_mfcc_features_from_flac(audio_file)
    user_model = {'username': username, 'features': features}

    # 모델 저장 경로 설정
    model_folder = f"C:\\voice\\models\\{username}"
    os.makedirs(model_folder, exist_ok=True)
    model_path = os.path.join(model_folder, f"{username}_model.pkl")

    # 모델 저장
    with open(model_path, 'wb') as f:
        pickle.dump(user_model, f)
    print(f"{username}'s model has been saved at {model_path}.")


# 사용자 인증 함수
def authenticate_user(audio_file, registered_user_model):
    input_features = extract_mfcc_features_from_flac(audio_file)

    # 등록된 사용자 모델 불러오기
    with open(registered_user_model, 'rb') as f:
        user_model = pickle.load(f)

    # 코사인 유사도로 음성 인증
    similarity = cosine_similarity([input_features], [user_model['features']])

    if similarity[0][0] >= 0.8:
        print(f"Authentication successful for {user_model['username']}.")
        return True
    else:
        print("Authentication failed.")
        return False


# 음성 녹음 함수
def record_audio(filename, duration=5):
    p = pyaudio.PyAudio()
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    frames_per_buffer = 1024

    # 녹음 시작
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=frames_per_buffer)

    print("Recording...")
    frames = []
    for _ in range(0, int(rate / frames_per_buffer * duration)):
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 녹음된 파일을 FLAC 형식으로 저장
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))


# 로그인 인증 예시
def authenticate_for_login(username):
    model_folder = f"C:\\voice\\models\\{username}"

    # 사용자 모델이 등록되지 않았다면 로그인 실패
    if not os.path.exists(model_folder):
        print(f"User '{username}' is not registered.")
        return

    # 사용자가 음성을 말하고 녹음
    audio_file_to_authenticate = f"C:\\voice\\wav\\{username}_login.wav"  # 로그인용 음성 파일 이름
    print("말씀하세요. 녹음중입니다.")
    record_audio(audio_file_to_authenticate, duration=5)  # 5초간 녹음

    # 등록된 사용자 모델 경로
    registered_user_model = os.path.join(model_folder, f"{username}_model.pkl")  # 저장된 모델 파일
    authenticate_user(audio_file_to_authenticate, registered_user_model)


# 사용자 등록 예시
def register_user(username):
    # 사용자 음성 파일 경로
    audio_file = f"C:\\voice\\wav\\{username}_register.flac"  # 예시로 `Amy1.wav`와 같은 기존 음성 파일을 사용
    print(f"회원가입을 위해 {username}님의 음성을 말해주세요.")
    record_audio(audio_file, duration=5)  # 5초간 음성 녹음
    save_user_model(username, audio_file)
    print(f"{username}님의 음성 등록이 완료되었습니다.\n")


# 메인 메뉴
def main():
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 로그인")
        print("2. 회원가입")
        print("0. 종료")
        choice = input("선택 (1/2/0): ")

        if choice == '1':
            username = input("로그인할 사용자 이름을 입력하세요: ")
            authenticate_for_login(username)  # 로그인 시도

        elif choice == '2':
            username = input("회원가입할 사용자 이름을 입력하세요: ")
            register_user(username)  # 회원가입 진행

        elif choice == '0':
            print("프로그램을 종료합니다.")
            break  # 프로그램 종료

        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")


# 프로그램 실행
if __name__ == "__main__":
    main()
