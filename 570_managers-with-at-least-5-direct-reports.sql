/* https://leetcode.com/problems/managers-with-at-least-5-direct-reports */
/* Write your T-SQL query statement below */
select e1.name
from employee e1 
join employee e2 on e1.id = e2.managerId
group by e1.id, e1.name
having count(*) >= 5