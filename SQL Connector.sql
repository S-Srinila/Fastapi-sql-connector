create database expenses_db;
use expenses_db;

create table expenses(
       id int auto_increment primary key,
       title varchar(50),
       amount float,
       category varchar(50)
       );

ALTER TABLE expenses 
ADD COLUMN description VARCHAR(255) AFTER id;

describe expenses;
show databases;
drop database expenses_db;


DROP DATABASE expenses_db;
CREATE DATABASE expenses_db;
USE expenses_db;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(50),
    description VARCHAR(255),
    amount FLOAT,
    category VARCHAR(50),
    date DATE
);
