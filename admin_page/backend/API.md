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