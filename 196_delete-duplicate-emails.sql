/*
https://leetcode.com/problems/delete-duplicate-emails/
 */
DELETE person where id in (
select p1.id FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id)