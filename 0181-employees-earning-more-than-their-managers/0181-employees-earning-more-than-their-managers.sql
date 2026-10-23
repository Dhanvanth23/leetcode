# Write your MySQL query statement below
Select e1.name as Employee
from Employee e1 left join Employee e2
on e1.managerId=e2.Id
where e1.salary > e2.salary