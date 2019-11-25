-- July and August temps
-- Return the highest 3 July and August temperature averages
SELECT city, avg_temp FROM (SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_temp DESC) AS julaugtemps LIMIT 3;
