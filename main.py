import librosa
import numpy as np
import pyaudio
import wave
import os
import tensorflow as tf
import tensorflow_hub as hub
from keras import layers
from keras import models

import pickle
import soundfile as sf  # FLAC 파일을 읽기 위한 라이브러리 추가
import noisereduce as nr  # 노이즈 제거 라이브러리


# FLAC 파일에서 MFCC 특징 추출 함수
def extract_mfcc_features_from_flac(audio_file):
    # FLAC 파일을 librosa로 처리하기 위해 soundfile 사용
    y, sr = sf.read(audio_file)
    y, _ = librosa.effects.trim(y)  # 앞뒤로 불필요한 침묵 제거
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)  # 평균으로 특징 벡터 추출
    return mfcc_mean


# RNN 모델 정의
def create_rnn_model(input_shape):
    model = models.Sequential()
    model.add(layers.Input(shape=input_shape))  # 입력 형태: (시간 단계, 특징 수)
    model.add(layers.SimpleRNN(64, activation='relu', return_sequences=False))  # RNN 층
    model.add(layers.Dense(32, activation='relu'))  # Dense 층
    model.add(layers.Dense(1, activation='sigmoid'))  # 이진 분류 (로그인 성공/실패)

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


# 사용자 음성 녹음 함수
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

    # 녹음된 파일을 WAV 형식으로 저장
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    # WAV 파일로 저장한 후 노이즈 제거
    reduce_noise_from_audio(filename)


def reduce_noise_from_audio(filename):
    # 파일을 librosa로 읽기
    y, sr = librosa.load(filename, sr=16000)

    # 노이즈 제거
    reduced_noise = nr.reduce_noise(y=y, sr=sr)

    # 노이즈가 제거된 음성을 파일로 저장
    sf.write(filename, reduced_noise, sr)
    print(f"Noise reduction applied to {filename}.")


# 사용자 모델 저장 함수
def save_user_model(username, audio_file):
    features = extract_mfcc_features_from_flac(audio_file)
    user_model = {'username': username, 'features': features}

    # 모델 저장 경로 설정
    model_folder = f"C:\\AI\\audio\\{username}"
    os.makedirs(model_folder, exist_ok=True)
    model_path = os.path.join(model_folder, f"{username}_model.pkl")

    # 모델 저장
    with open(model_path, 'wb') as f:
        pickle.dump(user_model, f)
    print(f"{username}'s model has been saved at {model_path}.")


# 사용자 인증 함수 (RNN 모델 사용)
def authenticate_user_with_rnn(audio_file, model_path):
    # 사용자 음성에서 MFCC 특징 추출
    input_features = extract_mfcc_features_from_flac(audio_file)
    input_features = input_features.reshape((1, input_features.shape[0], 1))  # (1, 특징 수, 1)

    # 모델 불러오기
    model = tf.keras.models.load_model(model_path)

    # 예측
    prediction = model.predict(input_features)
    if prediction >= 0.8:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed.")
        return False


# 사용자 등록 함수 (RNN 모델 학습)
# 모델 학습에 사용할 데이터 수를 늘리는 예시
def register_user(username):
    # 여러 음성 데이터를 사용하여 학습하기
    audio_files = [f"C:\\AI\\audio\\{username}_register_{i}.flac" for i in range(5)]  # 5개의 음성 파일을 사용
    print(f"회원가입을 위해 {username}님의 음성을 여러 번 녹음해주세요.")

    features_list = []
    for i, audio_file in enumerate(audio_files):
        record_audio(audio_file, duration=5)  # 5초간 음성 녹음
        save_user_model(username, audio_file)
        features = extract_mfcc_features_from_flac(audio_file)
        features_list.append(features)

    # 모델 학습 준비
    print(f"{username}님의 음성을 기반으로 모델을 학습합니다.")
    features = np.array(features_list)
    features = features.reshape((features.shape[0], features.shape[1], 1))  # (샘플 수, 특징 수, 1)

    model = create_rnn_model(input_shape=(features.shape[1], 1))
    model.fit(features, np.array([1] * len(features)))  # 각 음성 파일에 대해 라벨을 1로 설정 (등록됨)

    # 모델 저장
    model.save(f"C:\\AI\\models\\{username}\\voice_authentication_model.h5")
    print(f"{username}님의 음성 모델이 학습되어 저장되었습니다.\n")


# 로그인 인증 함수
def authenticate_for_login_with_rnn(username):
    model_folder = f"C:\\AI\\models\\{username}"

    # 사용자 모델이 등록되지 않았다면 로그인 실패
    if not os.path.exists(model_folder):
        print(f"User '{username}' is not registered.")
        return

    # 사용자 모델이 이미 등록 됐다면 username 이미 등록 됐다고 반환
    if os.path.exists(model_folder):
        print(f"User '{username}' is already registered.")
        return

    # 사용자가 음성을 말하고 녹음
    audio_file_to_authenticate = f"C:\\AI\\audio\\{username}_login.wav"  # 로그인용 음성 파일 이름
    print("말씀하세요. 녹음중입니다.")
    record_audio(audio_file_to_authenticate, duration=7)  # 5초간 녹음

    # RNN 모델 경로
    rnn_model_path = os.path.join(model_folder, 'voice_authentication_model.h5')  # 저장된 RNN 모델 파일
    authenticate_user_with_rnn(audio_file_to_authenticate, rnn_model_path)


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
            authenticate_for_login_with_rnn(username)  # 로그인 시도

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
