# Write your MySQL query statement below

#Make first char capital, rest lower
SELECT user_id, 
CONCAT(UPPER(SUBSTRING(name, 1, 1)), 
LOWER(SUBSTRING(name, 2))) 
AS name FROM Users
ORDER BY user_id;
