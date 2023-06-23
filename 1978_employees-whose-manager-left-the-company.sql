/* https://leetcode.com/problems/employees-whose-manager-left-the-company/ */
/* Write your T-SQL query statement below */
select employee_id 
from employees 
where salary < 30000
and manager_id not in (select employee_id from employees)
order by employee_id