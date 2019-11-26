-- Create db and table
-- Create db
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use db
USE `hbtn_0d_usa`;
-- Create unique_id table
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL);
