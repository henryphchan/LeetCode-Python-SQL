/* https://leetcode.com/problems/monthly-transactions-i/ */ 
/* Write your T-SQL query statement below */
select format(trans_date,'yyyy-MM') month,
       country,
       count(*) trans_count,
       sum(case state when 'approved' then 1 else 0 end) approved_count,
       sum(amount) trans_total_amount,
       sum(case state when 'approved' then amount else 0 end) approved_total_amount
from transactions
group by format(trans_date,'yyyy-MM'), country