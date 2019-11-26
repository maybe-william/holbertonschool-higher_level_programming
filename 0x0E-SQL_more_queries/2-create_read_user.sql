-- Create db and user
-- Create db
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
-- Create user_0d_1 with password user_0d_1_pwd and all priveleges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Set usage privileges
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
-- Set select privileges
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
