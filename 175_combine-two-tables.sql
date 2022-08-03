-- https://leetcode.com/problems/combine-two-tables/
/* Write your PL/SQL query statement below */
select p.firstname, p.lastname, a.city, a.state
from person p, address a
where p.personId = a.personId (+)