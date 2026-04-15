# Write your MySQL query statement below
SELECT 
    
    date_format(trans_date,'%Y-%m') AS month,
    country,
    count(trans_date) as trans_count,
    sum(case when state = "approved" then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount ,
    sum(case when state = "approved" then amount else 0 end) as approved_total_amount
FROM transactions
GROUP BY country, date_format(trans_date,'%Y-%m');