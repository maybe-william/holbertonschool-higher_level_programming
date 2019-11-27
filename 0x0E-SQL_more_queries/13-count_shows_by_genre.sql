-- Get a joined genre show db
-- Select query
SELECT t.name AS genre, COUNT(g.genre_id) AS number_of_shows FROM tv_genres t LEFT JOIN tv_show_genres g ON t.id = g.genre_id LEFT JOIN tv_shows s ON g.show_id = s.id GROUP BY genre ORDER BY number_of_shows DESC;
