DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id  INTEGER              NOT NULL,
  username VARCHAR (20)    NOT NULL,
  password VARCHAR (200)   NOT NULL,
  registration_time VARCHAR(30) NOT NULL
);
