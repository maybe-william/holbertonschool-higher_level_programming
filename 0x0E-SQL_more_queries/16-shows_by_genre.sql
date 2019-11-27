-- List all shows and associated genres
-- Select query
SELECT s.title, t.name FROM tv_shows s LEFT JOIN tv_show_genres g ON g.show_id = s.id LEFT JOIN tv_genres t ON t.id = g.genre_id ORDER BY s.title, t.name;
