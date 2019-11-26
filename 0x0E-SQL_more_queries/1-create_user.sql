-- Create user
-- Create user_0d_1 with password user_0d_1_pwd and all priveleges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Set all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
