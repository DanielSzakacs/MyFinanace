DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS financeData;

CREATE TABLE users(
  id  INTEGER  PRIMARY KEY NOT NULL,
  username VARCHAR (20)    NOT NULL,
  password VARCHAR (200)   NOT NULL,
  registration_time VARCHAR(30) NOT NULL
);

CREATE TABLE financeData(
  user_id INTEGER NOT NULL ,
  house INTEGER,
  food INTEGER,
  cloth INTEGER,
  everything_else INTEGER,
  income INTEGER
);

ALTER TABLE ONLY financeData
    ADD CONSTRAINT if_financeData_user_id FOREIGN KEY (user_id) REFERENCES users(id);