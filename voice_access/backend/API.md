# API info

### Deprecated
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

### 유저 등록
* 음성 등록 이전에 수행하는 작업
* 이름, 전화번호, 성별, 키, 몸무게
```
curl -X POST http://localhost:5000/api/user_register \
     -H "Content-Type: application/json" \
     -d '{
           "name": "홍길동",
           "phone": "010-1234-5678",
           "gender": "male",
           "height": 175.5,
           "weight": 68.2
         }'

{"error": "error 사유"}
{"message":"User registered successfully","user":{"gender":"male","height":175.5,"name":"\ud64d\uae38\ub3d9","phone":"010-1234-5678","weight":68.2}}
```
* 이름 50자 이하
* 전화번호는 dash 없는 형태
     * regex : "^0\d{1,2}-\d{3,4}-\d{4}$"
     * dash 필수
* 성별은 male 또는 female
* 키와 몸무게는 1~999

### 음성 등록
* 유저 정보 등록이 반드시 선행되어야 함
* 등록할 음성 업로드 (5회 수행)
     * count는 1 ~ 5
```
curl -X POST http://localhost:5000/api/voice_register/upload \
     -F "file=@sample.wav" \
     -F "uid=12345" \
     -F "count=3"

{"error": "Uploaded file not found"}
{"count":3,"message":"File upload successful"}

```

* 음성 등록 후 AI 처리 요청
```
curl -X POST http://localhost:5000/api/voice_register/call \
     -F "uid=12345"

{"error": "Uploaded file not found"}
{"status":"processing","uid":"12345"}
```
* AI 처리결과 조회
```
curl -X GET http://localhost:5000/api/voice_register/status \
     -F "uid=12345"

{"error": "No ID provided"}
{"result":false,"uid":"12345"}
```

# DB 요구사항
* 유저정보
     * 이름(50자 이하), 전번(대쉬포함 13자 이하), 성별(male/female), 키(3자리 이하 실수), 몸무게(3자리 이하 실수)
          * 실수 -> 소수점 이하 1자리
     * 등록날짜, 최종 업데이트 날짜
     * PK 지정이 필요 - 전화번호 등의 식별자에 대응하는 uid 생성이 필요
          * API 요청에 uid 통한 접근 예정
* 출입기록 로그
     * 유저 식별자, 입장/퇴장 여부, 시간, log_id
* 관리자 정보
     * 관리자 이름, 관리자 비번

## 추가 DB 요구사항
* ai 음성등록 과정 저장용
     * uid(FK, PK), 등록시간, 상태(True, False)
     * 재등록시 uid에 해당하는 기록 삭제할 필요도 존재
* ai 음성인증 대기열
     * uuid(PK, 16Byte), uid(FK), 등록시간, 상태(True, False)