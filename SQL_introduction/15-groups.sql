-- group by
SELECT COUNT(id),score AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
