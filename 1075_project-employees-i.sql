/* https://leetcode.com/problems/project-employees-i */
/* Write your T-SQL query statement below */
select p.project_id, round(avg(experience_years*1.0),2) average_years
from project p join employee e
on p.employee_id = e.employee_id
group by p.project_id