with rankedsales as (
    select name,departmentid,salary,
     DENSE_RANK() over (partition by departmentid order by salary desc) as rank
    from employee
)
select dep.name as "Department",emp.name as "Employee",emp.salary as "Salary"
from (select * from rankedsales where rank<=3) emp
inner join department dep on emp.departmentid=dep.id