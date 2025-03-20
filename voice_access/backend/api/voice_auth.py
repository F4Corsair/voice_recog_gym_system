from flask import jsonify, request
from werkzeug.utils import secure_filename
import uuid
from . import api_bp
import os

UPLOAD_PATH = "uploads/login"
ALLOWED_EXTENSIONS = {"wav"}

os.makedirs(UPLOAD_PATH, exist_ok=True)

def allowed_file(fname):
    return "." in fname and fname.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@api_bp.route("/voice_auth/upload", methods=["POST"])
def auth_upload_voice():
    if "file" not in request.files:
        return jsonify({"error": "File not found"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4()) # 고유 id 생성
        # file_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, filename)) # file hash 생성
        file_path = os.path.join(UPLOAD_PATH, file_id)

        file.save(file_path)

        # 대기열 DB 추가

        return jsonify({"message": "File upload successful", "file_id": file_id}), 201
    
    return jsonify({"error": "Invalid file type"}), 400

# 처리시간 길어지는 것 대비 분리
@api_bp.route("/voice_auth/result", methods=["GET"])
def get_result():
    file_id = request.form.get("file_id")
    if not file_id:
        return jsonify({"error": "No ID provided"}), 400

    # DB에서 로그인 기록 확인 - 10초 이내 로그인이라면 대기
    # 대기열 DB도 추가

    result = True

    # 파일 삭제 수행

    if result is None:
        return jsonify({"message": "Login in progress"}), 202
    

    return jsonify({"result": result}), 200