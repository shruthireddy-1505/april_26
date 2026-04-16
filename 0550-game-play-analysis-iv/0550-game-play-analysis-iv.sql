# Write your MySQL query statement below

SELECT 
    ROUND(
        COUNT(DISTINCT a.player_id) * 1.0 /
        (SELECT COUNT(DISTINCT player_id) FROM activity),
        2
    ) as fraction
FROM activity AS a
JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
) AS b
ON a.player_id = b.player_id
AND DATEDIFF(a.event_date, b.first_login) = 1 = 1;