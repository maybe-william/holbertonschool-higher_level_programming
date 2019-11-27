-- Count Dexter genres
-- Select query
SELECT t.name FROM tv_genres t INNER JOIN tv_show_genres g ON t.id = g.genre_id INNER JOIN tv_shows s ON g.show_id = s.id WHERE s.title = "Dexter" ORDER BY t.name ASC;
