from flask import jsonify, request
from threading import Thread
from . import api_bp
import os

# 유저 기본정보 등록 후 음성 5회 등록 ('고유 id + 회수'로 파일 구분)

UPLOAD_PATH = "uploads/register"
ALLOWED_EXTENSIONS = {"wav"}

os.makedirs(UPLOAD_PATH, exist_ok=True)

def allowed_file(fname):
    return "." in fname and fname.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def ai_task(uid):
    # 작업 후, 결과 DB에 저장
    return

@api_bp.route("/voice_register/upload", methods=["POST"])
def register_upload_voice():
    if "file" not in request.files:
        return jsonify({"error": "File not found"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    uid = request.form.get("uid")
    if not uid:
        return jsonify({"error": "No ID provided"}), 400
    
    count = request.form.get("count")
    if not count:
        return jsonify({"error": "No count provided"}), 400
    count = int(count)
    if count < 1 or count > 5:
        return jsonify({"error": "Count out of range", "count": count}), 400

    file_path = os.path.join(UPLOAD_PATH, uid + "_" + str(count))

    file.save(file_path)

    return jsonify({"message": "File upload successful", "count": count}), 201
    
# api/voice_register_upload 5회 수행 후 호출
@api_bp.route("/voice_register/call", methods=["POST"])
def register_voice():
    uid = request.form.get("uid")
    if not uid:
        return jsonify({"error": "No ID provided"}), 400
    
    for count in range(1, 6):
        file_path = os.path.join(UPLOAD_PATH, uid + "_" + str(count))

        if not os.path.exists(file_path):
            return jsonify({"error": "Uploaded file not found"}), 400
        
    thread = Thread(target=ai_task, args=(uid,))
    thread.start()

    return jsonify({"uid": uid, "status": "processing"}), 202

@api_bp.route("/voice_register/status")
def check_register_status():
    result = False

    uid = request.form.get("uid")
    if not uid:
        return jsonify({"error": "No ID provided"}), 400

    # DB에 음성 처리 여부 조회

    return jsonify({"uid": uid, "result": result})