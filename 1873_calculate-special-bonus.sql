/* https://leetcode.com/problems/calculate-special-bonus/ */
select employee_id, 
    case 
        when mod(employee_id,2) = 1 and substr(name,1,1) <> 'M' then salary 
        else 0 
    end "bonus"
from employees
order by employee_id