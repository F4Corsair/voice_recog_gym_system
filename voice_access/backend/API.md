# API info
```bash
# GET
curl -X GET http://localhost:5000/api/get
# POST
curl -X POST http://localhost:5000/api/post -H "Content-Type: application/json" -d '{"username": "test", "password": "1234"}'
```
* curl 사용한 API 테스트
* http:// 생략가능

```bash
curl -X POST http://localhost:5000/api/login \
     -H "Content-Type: application/json" \
     -d '{"username": "test", "password": "1234"}'
curl -X GET http://localhost:5000/api/protected \
     -H "Authorization: Bearer <access_token>"
curl -X POST http://localhost:5000/api/refresh \
     -H "Authorization: Bearer <refresh_token>"
```

```bash
curl -X POST http://localhost:5000/api/register \
     -H "Content-Type: application/json" \
     -d '{
           "name": "홍길동",
           "phone": "01012345678",
           "birthdate": "1995-06-15",
           "gender": "male",
           "height": 175.5,
           "weight": 68.2
         }'
curl -X GET http://localhost:5000/api/users
```

### 음성 로그인
* POST : login request
```
curl -X POST http://localhost:5000/api/voice_auth/upload \
     -F "file=@sample.wav"

{"error": "Invalid file type"}
{
  "message": "File uploaded successfully",
  "file_id": "123e4567-e89b-12d3-a456-426614174000"
}
```
* GET : login result
```
curl -X GET http://localhost:5000/api/voice_auth/result \
     -F "file_id=123e4567-e89b-12d3-a456-426614174000"

{"error": "No ID provided"}
{
  "message": "Processing in progress"
}
{
  "result": "True" or "False"
}
```

### 유저등록
* 등록할 음성 업로드 (5회 수행)
     * count는 1 ~ 5
```
curl -X POST http://localhost:5000/api/voice_register/upload\
     -F "file=@sample.wav" \
     -F "uid=12345"
     -F "count=3"

{"error": "Uploaded file not found"}
{
  "message": "File uploaded successfully",
  "count": "3"
}

```

* 음성 등록 후 AI 처리 요청
```
curl -X POST http://localhost:5000/api/voice_register/call \
     -F "uid=1234"

{"error": "Uploaded file not found"}
{"uid": 1234, "status": "processing"}
```
* AI 처리결과 조회
```
curl -X GET http://localhost:5000/api/voice_register/status \
     -F "uid=1234"

{"error": "No ID provided"}
{"uid": 1234, "result": False}
```