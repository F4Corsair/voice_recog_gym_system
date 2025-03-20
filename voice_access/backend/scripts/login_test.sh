#!/bin/bash
cd /app
set -x

# voice_auth.py
curl -X POST http://localhost:5000/api/voice_auth/upload \
     -F "file=@/app/uploads/login/v1.wav"

# 동일한 file_id 보내어 로그인 결과 및 처리여부 확인
curl -X GET http://localhost:5000/api/voice_auth/result \
     -F "file_id=51d18081-4d77-562d-a5f6-bb1936cdd583"