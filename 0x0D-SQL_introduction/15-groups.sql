-- Count Different Scores 
-- Make a count of scores grouped by score
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
