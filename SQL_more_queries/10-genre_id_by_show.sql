-- Show
SELECT tv_shows.title, tv_show_genres.id AS genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id;
