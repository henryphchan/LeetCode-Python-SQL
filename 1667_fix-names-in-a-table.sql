/* https://leetcode.com/problems/fix-names-in-a-table/ */
select user_id, upper(substr(name,1,1)) || lower(substr(name,2)) name
from users
order by user_id