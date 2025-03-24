-- test for users table
insert into users (name, phone_num, birth_date, gender, height, weight, voice)
values 
('홍길동', '010-1234-5678', '1994-08-12', 'male', 167.8, 62.3, null),
('김철수', '010-5678-1234', '2004-12-29', 'male', 179.8, 70.2, null),
('제갈선우', '010-1256-3478', '2001-01-01', 'female', 170.3, 65.6, null);

insert into users (name, phone_num, birth_date, gender, height, weight, voice)
values ('홍길동', '010-9999-3333', '1989-12-12', 'male', 178.9, 80.5, null);

/* unique 확인용
insert into users (name, phone_num, birth_date, gender, height, weight, voice)
values ('이버그', '010-9999-3333', '1979-11-12', 'female', 178.9, 80.5, null);
*/

insert into users (name, phone_num, birth_date, gender, height, weight, voice)
values ('최버그', '010-1233-3333', '1979-11-12', 'female', 178.9, 80.5, null);
