-- Count genre ratings
-- Select query
SELECT t.name, SUM(r.rate) AS rating FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id INNER JOIN tv_shows s ON g.show_id = s.id INNER JOIN tv_show_ratings r ON r.show_id = s.id GROUP BY t.name ORDER BY rating DESC;
