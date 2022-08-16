/* https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/ */
/* Write your PL/SQL query statement below */
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3 