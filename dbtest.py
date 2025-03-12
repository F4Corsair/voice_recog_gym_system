import os

# 파일 존재 여부 확인
file_path = "C:\\voice\\wav\\Amy\\Amy1.flac"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    print(f"File found: {file_path}")
