CREATE DATABASE IF NOT EXISTS python;

USE python;

CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  CGPA DOUBLE NOT NULL
);

INSERT INTO users VALUES(22010111,"Salma Hassan Soliman",20,3.3779);
INSERT INTO users VALUES(22010125,"Abdelhamed Hassan",20,3.8653);
INSERT INTO users VALUES(22010394,"Mariam Mahmoud Hassan",20,3.8268);
INSERT INTO users VALUES(22011453,"Moatz Mohamed El-shimy",20,3.7333);
INSERT INTO users VALUES(22010149,"abdo moataz mohamed el-shimy",21,10.9387);
INSERT INTO users VALUES(22011657,"Talal Barek",21,1.9829);
INSERT INTO users VALUES(2201088,"mazen",21,2.74);
INSERT INTO users VALUES(22010482,"Marina Maged Magdy",20,3.9387);
INSERT INTO users VALUES(22010444,"weza",20,3.7);
INSERT INTO users VALUES(1,"ahmed",24,4.0);