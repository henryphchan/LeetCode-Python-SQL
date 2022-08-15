/* https://leetcode.com/problems/game-play-analysis-i/ */
/* Write your PL/SQL query statement below */
select player_id, to_char(event_date,'yyyy-mm-dd') "first_login"
from Activity a1
where event_date = (select min(event_date) from activity a2 where a1.player_id = a2.player_id)