DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id  INTEGER PRIMARY KEY NOT NULL,
  username VARCHAR (20)   NOT NULL,
  password VARCHAR (40)   NOT NULL
);