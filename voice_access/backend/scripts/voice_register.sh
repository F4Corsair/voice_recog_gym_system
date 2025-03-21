#!/bin/bash
cd /app
set -x

# user_register.py
curl -X POST http://localhost:35000/api/voice_register/upload \
     -F "file=@/app/uploads/register/v1.wav" \
     -F "uid=12345" \
     -F "count=1"

curl -X POST http://localhost:35000/api/voice_register/upload \
     -F "file=@/app/uploads/register/v2.wav" \
     -F "uid=12345" \
     -F "count=2"

curl -X POST http://localhost:35000/api/voice_register/upload \
     -F "file=@/app/uploads/register/v3.wav" \
     -F "uid=12345" \
     -F "count=3"

curl -X POST http://localhost:35000/api/voice_register/upload \
     -F "file=@/app/uploads/register/v4.wav" \
     -F "uid=12345" \
     -F "count=4"

curl -X POST http://localhost:35000/api/voice_register/upload \
     -F "file=@/app/uploads/register/v5.wav" \
     -F "uid=12345" \
     -F "count=5"

curl -X POST http://localhost:35000/api/voice_register/call \
     -F "uid=12345"

curl -X GET http://localhost:35000/api/voice_register/status \
     -F "uid=12345"