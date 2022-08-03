/* https://leetcode.com/problems/tree-node/ */
select id, 'Root' type
from tree
where p_id is null
union
select id, 'Inner' type
from tree
where id in (select p_id from tree where p_id is not null) and p_id is not null
union
select id, 'Leaf' type
from tree
where id not in (select p_id from tree where p_id is not null) and p_id is not null
