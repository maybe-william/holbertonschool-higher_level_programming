-- Count Dexter genres
-- Select query
SELECT DISTINCT s.title FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id RIGHT JOIN tv_shows s ON g.show_id = s.id WHERE s.title NOT IN (SELECT s.title FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id RIGHT JOIN tv_shows s ON g.show_id = s.id WHERE t.name = "Comedy") ORDER BY s.title ASC;
