# Write your MySQL query statement below
#Write an SQL query to report all customers who never order anything.

#Change name of output col to alias Customer
Select name AS 'Customers'
FROM Customers
#joins all the customers that did order
LEFT JOIN Orders
ON orders.customerId = Customers.id
#we get null as we want customers that never ordered 
WHERE orders.customerId IS NULL;
