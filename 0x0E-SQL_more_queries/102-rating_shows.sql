-- Rate shows
-- Select query
SELECT s.title, SUM(r.rate) AS rating FROM tv_shows s INNER JOIN tv_show_ratings r ON s.id = r.show_id GROUP BY s.id ORDER BY rating DESC;
