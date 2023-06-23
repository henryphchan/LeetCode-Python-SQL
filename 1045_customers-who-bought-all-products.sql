/* https://leetcode.com/problems/customers-who-bought-all-products */
/* Write your T-SQL query statement below */
select customer_id
from customer 
group by customer_id
having count(distinct product_key) = (select count(*) from product)
