# Write your MySQL query statement below

#Swap f with m and vice versa
UPDATE Salary
SET sex = CASE 
            WHEN sex = 'm' THEN 'f'
            WHEN sex = 'f' THEN 'm'
        END;
