/* https://leetcode.com/problems/average-selling-price */
/* Write your T-SQL query statement below */
select p.product_id, round(SUM(price*units)/cast(SUM(units) as decimal(7,2)),2) average_price
from prices p join unitssold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id