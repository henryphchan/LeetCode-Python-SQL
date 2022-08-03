-- https://leetcode.com/problems/second-highest-salary/
/* Write your PL/SQL query statement below */
select max(e.salary) SecondHighestSalary 
from Employee e
where e.salary <> (select max(e2.salary) from employee e2)