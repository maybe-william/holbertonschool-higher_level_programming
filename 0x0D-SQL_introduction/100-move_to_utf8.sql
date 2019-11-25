-- Convert
-- Convert DB to utf8mb4 and collate utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Select the database
USE hbtn_0c_0;
-- Convert first_table
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert the column
ALTER TABLE first_table CHANGE COLUMN name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
