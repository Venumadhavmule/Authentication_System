-- create_db.sql
CREATE DATABASE IF NOT EXISTS flask_auth_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- optional: create a dedicated user (change password!)
-- CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'flaskpassword';
-- GRANT ALL PRIVILEGES ON flask_auth_db.* TO 'flaskuser'@'localhost';
-- FLUSH PRIVILEGES;
