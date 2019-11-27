-- Count comedy shows
-- Select query
SELECT s.title FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id INNER JOIN tv_shows s ON g.show_id = s.id WHERE t.name = "Comedy" ORDER BY s.title ASC;
