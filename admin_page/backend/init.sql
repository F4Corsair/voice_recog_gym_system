-- CREATE USER 'user'@'%' IDENTIFIED BY 'password';
-- GRANT ALL ON *.* TO 'user'@'%';

-- create user table
create table users(
	order_id int auto_increment primary key,
	name varchar(8) not null,
	phone_num varchar(18) not null,
	birth_date DATE not null,
	gender varchar(10) not null,
	height float,
	weight float,
	voice varchar(200),
	unique (phone_num)
);

-- convert table to accept korean
ALTER TABLE users CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
