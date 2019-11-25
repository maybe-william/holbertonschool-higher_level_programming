-- Say My Name
-- List all records of Second table minus ones without a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
