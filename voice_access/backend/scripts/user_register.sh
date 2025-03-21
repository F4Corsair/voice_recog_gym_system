#!/bin/bash
cd /app
set -x

# user_register.py
curl -X POST http://localhost:35000/api/user_register \
     -H "Content-Type: application/json" \
     -d '{
           "name": "홍길동",
           "phone": "010-1234-5678",
           "gender": "male",
           "height": 175.5,
           "weight": 68.2
         }'