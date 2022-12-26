# Write your MySQL query statement below
#Write an SQL query to calculate the bonus of each employee. 
#The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. T
#he bonus of an employee is 0 otherwise.
 Select employee_id,
 CASE
    WHEN mod(employee_id,2) = 1
     AND name NOT LIKE 'M%'
     THEN salary
 ELSE
     0 END AS bonus
 FROM Employees
 ORDER BY employee_id;

