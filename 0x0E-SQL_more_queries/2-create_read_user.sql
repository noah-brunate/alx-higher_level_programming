-- script creates a database hbtn_0d_2 and
-- user hbtn_0d_2@localhost with SELECT privileges

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'htbn_0d_2'@'localhost' IDENTIFIED BY 'user_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'hbtn_0d_2'@'localhost';
FLUSH PRIVILEGES
