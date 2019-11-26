-- Create db and table
-- Create db
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use db
USE `hbtn_0d_usa`;
-- Create city table
CREATE TABLE IF NOT EXISTS cities(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
