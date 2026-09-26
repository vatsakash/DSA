# Write your MySQL query statement below
Select sell_date,COUNT(distinct(product)) AS num_sold,
group_concat(distinct product order by product asc separator ',')as products 
from Activities 
Group by sell_date 