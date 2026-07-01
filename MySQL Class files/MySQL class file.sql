# create a database db
create database db;

# now use it
use db;

# delete the database db
drop database db;

# create a customer table with name, age, balance, dob, sales
create table customer(
	name varchar(20),
    age tinyint,
    balance int,
    dob DATE,
    sales int
);


# delete a table
drop table customer;

# check the structure of a table
describe customer;

# to check the data in a table 
select * from customer;


# Create a table of sales with these columns - Order_id (A101), product, weight(5.67) , qty, sales?

# Create a table for library management system where there will be these table ?
# 1.Create a database Library
# 2.Create books_info table with - book_id, name, pages, writer, year
# 3.Create stock - book_id, total_books, issued, remaining

-- ---------------  Alter  ---------------------

# Add a new column address in customer table
alter table customer add column address varchar(100);

# Add a new column height in customer table


# Add a new column phone (bigint) in customer table
alter table customer add phone bigint;

# Now change the data type of phone to varchar(10)? 
alter table customer modify column phone varchar(10);

# change column name sales to amount?
alter table customer change column sales amount int;

# delete column balance ?
alter table customer drop column balance;

# change the table name customer to new_customer?
alter table customer rename to new_customer;

# delete the table customer
drop table new_customer;

-- ---------------------------- DML --------------------------------

create table emp(
	name varchar(30),
    age int,
    salary int
);

# enter a single record
insert into emp
values ("rohan",24,50000);

# show all the data in emp table
select * from emp;

# insert multiple records in emp table
insert into emp
values ("kunal",28,23000),("suman",56,50600),("kartik",12,23000);


insert into emp(name,age)
values ("mohit",49);

insert into emp
values ("sumit",null,99000);

insert into emp
values (null,null,null);

select * from emp;

# update a record in emp table where name is rohan and set age to 13
update emp
set age = 13
where name = "rohan";

update emp
set age = 50;

select * from emp;

# delete a record from emp table where name is mohit
delete from emp
where name = "mohit";

delete from emp
where salary < 30000;

# delete all records from emp table
truncate table emp;

delete from emp
where salary > 40000;

select * from emp;

describe emp;

show create table emp;

-- --------------------TCL-------------------------------
-- --- ACID -------
/*
    ACID Properties in Database Systems
    
    ACID is an acronym that represents four key properties of reliable database transactions:
    
    1. ATOMICITY
         - Ensures that a transaction is "all-or-nothing"
         - Either all operations within a transaction complete successfully, or none of them do
         - If a failure occurs mid-transaction, all changes are rolled back to maintain data consistency
         - Example: Money transfer must either debit from one account AND credit to another, or neither happens
    
    2. CONSISTENCY
         - Guarantees that a transaction takes the database from one valid state to another valid state
         - All data integrity rules and constraints are maintained before and after the transaction
         - The database will never be left in a partially updated or corrupted state
         - Example: Total balance in all accounts must remain constant during a transfer
    
    3. ISOLATION
         - Ensures that concurrent transactions do not interfere with each other
         - Each transaction executes independently without visibility into uncommitted changes from other transactions
         - Example: Two simultaneous transactions on the same data won't cause conflicts
    
    4. DURABILITY
         - Guarantees that once a transaction is committed, the data persists permanently
         - Even in case of system failures, power outages, or crashes, committed changes survive
         - Data is stored in persistent storage (disk) and cannot be lost after commit
         - Example: Once a purchase is confirmed, it remains in the database even if the server crashes
    
    ACID properties are essential for maintaining data reliability and integrity in critical applications.
*/

create table bank(
	name varchar(30),
    amount int 
    );
    
insert into bank values ("ravi",500), ("kunal",1000);

select * from bank;

start transaction ;

update bank
set amount = amount - 200
where name = "ravi";

update bank
set amount = amount + 200
where name = "kunal";

rollback ;

savepoint hello;

delete from bank;

rollback to hello;

select * from bank;

truncate table bank;

commit;
-- ------------------ CONSTRAINT ----------------
CREATE table test (
	name varchar(30) not null,
    phone int unique,
    city varchar(30) default "indore"
    );

insert into test values("ravi",999,"bhopal");
insert into test values("ravi",999,"bhopal");
insert into test values(null,888,"bhopal");
insert into test(name) values("mohit");
insert into test values("mohan",777,null);

select * from test;



-- --------------------- DQL ---------------
-- DQL (Data Query Language) is a subset of SQL used to retrieve and query data from databases.
-- Common DQL commands include SELECT, which allows you to fetch data from one or more tables
-- with various filtering, sorting, and aggregation options.


select * from store;


# select - use to show anything on screen

select 870 ;

select "hello world" as msg ;

select "Mohan" as name, 45 as age;

select name,city as location ,sales from store;

select name as customer_name from store;

# select with calculations
select name,sales,profit,sales-profit as cost from store;

#    functions


select concat(name, " ", category) as full_name from store;

# make a sales category column?
select sales,if(sales>1000,"good","bad") as sales_category from store;

# make a profit category( profit / loss ) column?

select 
	profit,
    if(profit>0,"profit","loss") as profit_category
from store; 

# Aggfunc - sum, min, max, count, avg
select sum(sales),min(sales),max(sales)
from store;

# find total profit


# find avg of qty

# find total number of orders?
select count(*) from store;

select count(post_code) from store;

# find the profit margin of orders and round it to 2 decimal places?
select round(sum(profit) / sum(sales) * 100,2) as profit_margin
from store;


# year - month - day functions
select 
	order_date, 
    year(order_date),
    month(order_date),
    day(order_date),
    monthname(order_date),
    dayname(order_date)
from store;

# Difference between two dates (to calculate age)?
select timestampdiff(month, order_date, current_date())
from store;

select concat(name," ",state) from store;


# select distinct 
select distinct category  from store;

select distinct category,sub_category from store;

select count(distinct city) from store;

# Q Find number of unique customers ?


select distinct * from store ;


# Where 

select name,sales
from store
where sales>2000;

select * 
from store
where region = "east";

# Select all the records of furniture category ?
# Show name, sales and profit the records where we have loss ?
# Show all the transaction from year 2015 ?


# 	AND - OR 
# Show customer name category sales and profit where the category is Furniture and we had face a loss ?
select name, category ,sales , profit
from store
where category = "furniture"  and profit<0 ;

# Show all the customer name region and sales where either the region should be East or the sales should be above 1000 ?


# show sales column where the sales is between 20 and 25 ?
select sales
from store
where sales > 20 and sales <25;

select sales
from store
where sales between 20 and 25;

# filter null values
select * from store
where post_code is null;

select * from store
where post_code is not null;

# Count number of null values in post_code ?
select count(*)
from store
where post_code is null;

# Find total sales in Technology category?



select round(sales,2) from store;

select * from students ;


select sub_category , sum(sales)
from store
group by sub_category;

select region,category , sum(sales)
from store
group by region,category
order by region, category ;



select month(order_date) as month , count(*) as cnt
from store
where category = "furniture"
group by month ;

# CASE - WHEN - THEN - ELSE - END
select sales , 
	case 
		when sales < 500 then "Low"
		when sales < 1000 then "Mid"
		when sales < 2000 then "High"
        else "Very High"
    end as sales_category
from store
order by sales desc;


# select with having clause

select sub_category, sum(sales) as total_sales
from store
group by sub_category
having total_sales < 1000;

-- -------------------Windows Functions -----------------------
select name,region,sales,rank() over (partition by region order by sales desc ) as ranking
from store;

select * ,rank() over(partition by gender , department order by marks desc) as ranking
from students;


select * , 
	rank() over(order by scholarship desc) as rank_func,
	dense_rank() over(order by scholarship desc) as dense_rank_func,
    ROW_NUMBER() over(order by scholarship desc) as row_number_func
    
from students;



-- create table
create table yearly_sales (
    sales_year int,
    sales_amount int
);

-- insert sample data
insert into yearly_sales (sales_year, sales_amount)
values
(2018, 42000.00),
(2019, 44500.00),
(2020, 39800.00),
(2021, 46250.00),
(2022, 48700.00),
(2023, 51500.00),
(2024, 53800.00),
(2025, 55600.00);

-- view data
select * 
from yearly_sales;

select * , lag(sales_amount) over() as prv_sales , sales_amount - lag(sales_amount) over() as changes
from yearly_sales;

select * , lead(sales_amount) over() as nxt_sales 
from yearly_sales;

-- --------------------Practice Questions -------------------

-- create table
create table students (
    student_id int primary key,
    student_name varchar(50),
    gender varchar(10),
    age int,
    department varchar(30),
    semester int,
    city varchar(30),
    marks decimal(5,2),
    scholarship decimal(10,2)
);

-- insert records
insert into students values
(101, 'arjun', 'male', 20, 'computer science', 3, 'indore', 85.50, 5000),
(102, 'priya', 'female', 19, 'computer science', 2, 'bhopal', 91.00, 8000),
(103, 'rohan', 'male', 21, 'mechanical', 5, 'indore', 72.50, 3000),
(104, 'neha', 'female', 20, 'civil', 4, 'ujjain', 88.00, 6000),
(105, 'amit', 'male', 22, 'electrical', 6, 'dewas', 67.00, 2000),
(106, 'kavya', 'female', 18, 'computer science', 1, 'bhopal', 95.50, 10000),
(107, 'vivek', 'male', 23, 'mechanical', 7, 'indore', 78.00, 4000),
(108, 'pooja', 'female', 21, 'civil', 5, 'ratlam', 82.00, 5000),
(109, 'rahul', 'male', 20, 'electrical', 3, 'ujjain', 74.50, 2500),
(110, 'sneha', 'female', 22, 'computer science', 6, 'bhopal', 89.50, 7000),
(111, 'deepak', 'male', 19, 'civil', 2, 'indore', 65.00, 1500),
(112, 'anjali', 'female', 20, 'mechanical', 4, 'dewas', 93.00, 9000),
(113, 'manish', 'male', 21, 'computer science', 5, 'ratlam', 80.50, 4500),
(114, 'riya', 'female', 18, 'electrical', 1, 'bhopal', 97.00, 12000),
(115, 'sachin', 'male', 22, 'civil', 6, 'indore', 70.00, 2500),
(116, 'nisha', 'female', 19, 'computer science', 2, 'ujjain', 86.00, 5500),
(117, 'akash', 'male', 20, 'mechanical', 3, 'dewas', 76.50, 3000),
(118, 'meera', 'female', 21, 'civil', 5, 'ratlam', 90.00, 8500),
(119, 'karan', 'male', 23, 'electrical', 7, 'bhopal', 68.00, 2000),
(120, 'simran', 'female', 22, 'computer science', 6, 'indore', 92.50, 9500);

-- view all records
select * from students;

-- 1. display all students

-- 2. display only student_name and marks

-- 3. display all female students

-- 4. display students from indore

-- 5. display students whose marks are greater than 85

-- 6. display students whose age is less than 20

-- 7. display unique cities

-- 8. display unique departments

-- 9. display students sorted by marks in ascending order

-- 10. display students sorted by marks in descending order

-- 11. display top 5 students based on marks

-- 12. display students whose marks are between 80 and 90

-- 13. display students whose age is between 19 and 21

-- 14. display students from indore, bhopal and ujjain

-- 15. display students from civil and mechanical departments

-- 16. display students whose names start with 'a'

-- 17. display students whose names end with 'a'

-- 18. display students whose names contain 'an'

-- 19. display total number of students

-- 20. display average marks

-- 21. display highest marks

-- 22. display lowest marks

-- 23. display total scholarship amount

-- 24. count students department wise

-- 25. display average marks department wise

-- 26. display total scholarship city wise

-- 27. display departments having average marks greater than 80

-- 28. display cities having more than 3 students

-- 29. display students whose scholarship is greater than 5000

-- 30. display top 3 students with highest scholarship


-- --------------------Joins in MySQL -------------------

-- create department table
create table departments (
    department_id int primary key,
    department_name varchar(50),
    location varchar(50)
);

-- create employee table
create table employees (
    employee_id int primary key,
    employee_name varchar(50),
    salary decimal(10,2),
    department_id int,
    manager_id int
);

-- insert departments
insert into departments values
(1, 'hr', 'indore'),
(2, 'finance', 'bhopal'),
(3, 'it', 'pune'),
(4, 'marketing', 'mumbai'),
(5, 'sales', 'delhi'),
(6, 'research', 'hyderabad');

-- insert employees
insert into employees values
(101, 'arjun', 80000, 1, null),
(102, 'priya', 55000, 2, 101),
(103, 'rohan', 60000, 3, 101),
(104, 'neha', 48000, 3, 102),
(105, 'amit', 52000, 5, 102),
(106, 'kavya', 65000, 2, 101),
(107, 'vivek', 70000, 4, 103),
(108, 'pooja', 47000, 1, 103),
(109, 'rahul', 58000, null, 101),
(110, 'sneha', 62000, null, 106);

-- view data
select * from departments;
select * from employees;

-- 1. display employee name and department name using inner join

-- 2. display all employees whether department exists or not

-- 3. display all departments whether employees exist or not

-- 4. display employee name, salary and department name

-- 5. display employees working in it department

-- 6. display employees whose department location is pune

-- 7. count employees department wise

-- 8. display average salary department wise

-- 9. display departments having more than 1 employee

-- 10. display department with highest average salary

-- 11. display all employee-department combinations using cross join

-- 12. display employee and manager names using self join

-- 13. display employees who are not assigned to any department

-- 14. display departments that have no employees
select *
from departments left join employees
on employees.department_id = departments.department_id
where employee_id is null;

-- 15. display employee name, department name and location




