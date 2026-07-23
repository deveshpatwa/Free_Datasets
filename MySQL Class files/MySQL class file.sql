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
alter table customer add column phone bigint;

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
values(" ",99,15000);

insert into emp
values ("sumit",null,99000);

insert into emp
values (null,45,99000);

insert into emp
values ('null',45,99000);

insert into emp
values (null,null,null);

select * from emp;

# update a record in emp table where name is rohan and set age to 13
update emp
set age = 13
where name = "rohan";


update emp
set age = 55;

select * from emp;

set sql_safe_updates = 0;

# delete a record from emp table where name is mohit
select * from emp;

delete from emp
where name = "mohit";

delete from emp;

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

-- ---- NOT NULL , UNIQUE , DEFAULT ---------------
drop table test;

CREATE table test (
	name varchar(30) not null,
    phone int unique,
    city varchar(30) default "indore"
    );

describe test;

insert into test values("ravi",999,"bhopal");
insert into test values("suman",999,"itarsi");
insert into test values(null,888,"bhopal");
insert into test(name) values("mohit");
insert into test values("mohan",777,null);

select * from test;

-- ----------- CHECK ---------------
drop table vote;

create table vote (
	name varchar(30),
    age int,
    constraint check_age check (age>=18)
    );
	
describe vote;

show create table vote;

insert into vote values ("kunal",24);
insert into vote values ("mohit",15);

select * from vote;

-- ------------AUTO_INCREMENT ---------------

drop table people;

create table people(
	id int unique AUTO_INCREMENT,
    name varchar(30)
    );

describe people;

insert into people(name) values ("rohan"),("kunal"),("mohit");

select * from people;

DELETE from people;

insert into people(name) values ("umang");

truncate table people;

-- ----------------- PRIMARY KEY
drop table customer;
drop table orders;


create table customer(
	customer_id int primary key,
    name varchar(30)
    );

describe customer;
	
-- -----------Foreign Key ---------------- 
create table orders(
	product_name varchar(30),
    amount int,
    customer_id int, 
    foreign key(customer_id) references customer(customer_id)
    );
  

insert into customer values(1,"rohan"),(2,"kunal");

select * from customer;

insert into orders values("apple",400,2); 
insert into orders values("Banana",670,4);
insert into orders values("Banana",670,null);
select * from orders;
  
describe orders;  
  
show create table orders;


-- --------------------- DQL ---------------
-- DQL (Data Query Language) is a subset of SQL used to retrieve and query data from databases.
-- Common DQL commands include SELECT, which allows you to fetch data from one or more tables
-- with various filtering, sorting, and aggregation options.


select * from store;

-- ------------------ select -----------------

select 870 ;

select 67*2 ;

select "hello world" as msg ;

select "Mohan" as name, 45 as age;

select name,sales,sales*0.8 as discounted_sales from store;


select name,city as location ,sales from store;

select name as customer_name from store;

-- -------------select with calculations
select name,sales,profit,sales-profit as cost from store;

-- ---------------- functions

-- --------- Text Functions
select upper(name),name from store;
select lower(name) from store;

select left(name,2) from store;
select name,right(name,3) from store;

select concat("Rohan"," ","Kumar") as full_name;

select length(name),name from store;

select concat(name , " " , category) as full_name from store;

select state , city from store;


# make a sales category column?

select sales,if(sales>1000,"good","bad") as sales_category from store;

# make a profit category( profit / loss ) column?
select profit from store;


select 
	profit,
    if(profit>0,"profit","loss") as profit_category
from store; 

select sales, round( if(sales>1000,sales*0.10,sales*0.05),2) as discount
from store;


-- ---------------CASE - WHEN - THEN - ELSE - END
select sales , 
	case 
		when sales < 500 then "Low"
		when sales < 1000 then "Mid"
		when sales < 2000 then "High"
        else "Very High"
    end as sales_category
from store;

# create a column for profit category - Loss, low profit , high profit, very high profit ?
select profit from store;


-- ------------ Aggfunc - sum, min, max, count, avg
SELECT 
    SUM(sales) AS total_sales,
    MIN(sales),
    MAX(sales),
    COUNT(sales),
    AVG(sales)
FROM
    store;

# find total profit

# find avg of qty and round them to 2 decimal places 

# find total number of orders?
select count(*) from store;

select count(post_code) from store;

# find the profit margin of orders and round it to 2 decimal places?
select round(sum(profit) / sum(sales) * 100,2) as profit_margin
from store;

# Find average unit price (sales/qty) and round it to 2 decimal places



-- --------------- year - month - day functions
select 
	order_date, 
    year(order_date),
    month(order_date),
    day(order_date),
    monthname(order_date),
    dayname(order_date),
    now(),
    current_date(),
    current_time()
from store;

-- ---------TIMESTAMPDIFF 
select order_date as DOB, timestampdiff(year, order_date, current_date()) as AGE
from store;


select order_date, 
	concat(
    timestampdiff(year , order_date,current_date()), " years and ",
    mod( timestampdiff(month , order_date,current_date()) , 12), " months") as age
from store;

select concat(  round(sum(sales) / 1000,2) , " K") as total_sales
from store;


 -- -------- select distinct 

select category from store;

select distinct category  from store;

# Find all the unique customers name from store ?

select count(distinct category)  from store;

select distinct category,sub_category from store;

select count(distinct city) from store;

select  distinct * from store ;

-- -------SELECT  WHERE 

select *
from store
where sub_category = "chairs";

# Find total sales in furniture category ?
select sum(sales) as total_sales
from store
where category = "furniture";

# Select all the records where the category should not be furniture ?
select *
from store
where category != "furniture";


select name,sales
from store
where sales>=2000;

select * 
from store
where region = "east";

# Select all the records of furniture category ?
# Show name, sales and profit the records where we have loss ?
# Show all the transaction from year 2015 ?
# Find total sales in 2016 ?
# Find average profit in furniture category ?

-- -------------WHERE WITH 	AND - OR 

# Show customer name, category, sales, profit and there cost where the category is Furniture and we had face a loss ?
select name, category ,sales , profit,round(sales-profit,1) as cost
from store
where category = "furniture"  and profit<0 ;

# Show all the customer name region and sales where either the region should be East or the sales should be above 1000 ?


-- ---------SELECT WHERE  BETWEEN
# show sales column where the sales is between 20 and 25 ?
select sales
from store
where sales > 20 and sales <25;

select sales
from store
where sales between 20 and 25;


-- ---------SELECT WHERE  NULL AND NOT NULL
# filter null values
select * from store
where post_code is null;

select * from store
where post_code is not null;

# Count number of null values in post_code ?
select count(*)
from store
where post_code is null;


-- --------------- WHERE LIKE

# Show all the unique names which starts with "A"
SELECT distinct name
from store
where name like "a%";

# Find all the unique name which start with "T" and ends with "s"?
SELECT distinct name
from store
where name like "t%s";

# Find all the unique name which ends with "sh"
# Show name column where the customer name start with 'P'?
# Show name column from store where the customer name end with "gh"

# Find all the unique sub_category which start with "A" and has total 3 char?
select distinct sub_category
from store
where sub_category like "a__";

# Find if like works on numeric values? 

-- ------------- WHERE  IN , NOT IN

select name, sub_category,sales
from store
where sub_category in ("art","paper","tables");

select name, sub_category,sales
from store
where sub_category NOT in ("art","paper","tables");

-- ------------------ GROUP BY
-- for single column
select region,sales from store;

# show region wise total sales ?
select region, sum(sales)
from store
group by region;

# Find city wise total profit and total sales ?
select city , round(sum(sales)), round(sum(profit))
from store
group by city;

# Show gender wise average marks from students table?

# Show department wise average marks for each gender ?

# Show sub_category wise total sales and total profit ?

# Find category wise number of orders ?


-- --------------group by with multiple columns

# Show category wise total sales for each region ?
select region,category, sum(sales)
from store
group by region , category;

# Show category then subcategory by total sales, total profit and average quantity ?


-- ------------------ HAVING -------------------

# show subcategory wise total sales where the total sales is less then 1000?
select sub_category, round(sum(sales)) as total_sales
from store
where total_sales < 1000
group by sub_category;


select sub_category, round(sum(sales)) as total_sales
from store
group by sub_category
having total_sales < 1000;

# Find department wise Average marks ?
select  department , avg(marks) as percentage
from students
group by department
having percentage > 85;


-- ------------HAVING VS WHERE

select category, round(sum(sales)) as total_sales
from store
where category = "furniture"
group by category;


select category, round(sum(sales)) as total_sales
from store
group by category
having category = "furniture";



# Find all the subcategories where the total profit is in negative ?
# Find category wise total sales where the total sales is less than 30,000 ?


-- ------------------ ORDER BY

select * from store;

# show all the records from store table in ascending order of order_date ?
SELECT *
from store
order by order_date asc ;

# Show subcategory wise total sales and order them in descending order ?
select sub_category , round(sum(sales)) as total_sales
from store
group by sub_category
order by total_sales desc;

-- -----------order by with 2 columns
select * 
from store
order by category,sub_category,sales desc ;

-- ---------------- limit 
select * 
from store
limit 3;

# Top three translation with highest sales in east region?
select *
from store
where region = "east"
order by sales desc
limit 3;


# Show name region and profit column where the name should start with "S" and the region should be "East" and show only top 10 transactions with highest profit ?


# Find top 2nd person with the highest total sales ?
select name, round(sum(sales)) as total_sales
from store
group by name
order by total_sales desc
limit 1 offset 1;

select name, round(sum(sales)) as total_sales
from store
group by name
order by total_sales desc
limit 4,1;

select name, round(sum(sales)) as total_sales
from store
group by name
order by total_sales desc
limit 1 offset 4;

# Find the customer who has the longest name ?


-- -----------------JOINS -------------------------------
select * from employee;
select * from department;

select *
from employee inner join department
on employee.department_id = department.department_id;

-- using there full names 
select employee.name, employee.salary, department.name as department
from employee inner join department
on employee.department_id = department.department_id;

# using short names
select e.employee_id, e.name,e.salary,d.name
from employee as e inner join department as d
on e.department_id = d.department_id;


-- left join
select * 
from employee left join department
on employee.department_id = department.department_id;

-- right join
select * 
from employee right join department
on employee.department_id = department.department_id;

# full join

select * 
from employee left join department
on employee.department_id = department.department_id
union 
select * 
from employee right join department
on employee.department_id = department.department_id;

# cross join 
select * 
from employee , department;

select *
from employee cross join department;

# self join
select emp.name as employee , coalesce(manager.name,"No manager")    as manager
from employee as emp left join employee as manager
on emp.manager_id = manager.employee_id;


# Show all the employees whose department head is Rakesh ?


-- ----------------- UNION -------------------------------
select * from sales_2019
union
select * from sales_2020
union
select * from sales_2021;

-- union all
select * from sales_2019
union 
select * from sales_2020
union 
select * from sales_2021
union all
select * from sales_2021;


select month,salesamount from sales_2019
union 
select region,salesamount from sales_2020;


-- ------------------SUB-QUERY ---------------------------
-- When the output of a sub query is a single value ?
select * from students;

select avg(marks) from students;

# Find the students with above average marks ?
select * 
from students
where marks > (select avg(marks) from students )
order by marks ;

# Find a student with the highest marks ?



-- When the output is a single column ?
# Show all the transaction of customers who have made a transaction of above 1000 in their lifetime ?
select * from store;

select distinct name
from store
where sales > 1000;

select * 
from store
where name in (select distinct name from store where sales > 1000) ; 

-- when you have a table as a output
# Show how many number of orders are of profit or loss ?
select profit, if(profit>0,"Profit","Loss") as pnl from store;

select pnl,count(*)
from (select profit, if(profit>0,"Profit","Loss") as pnl from store) as temp
group by pnl;

-- -------------------WITH (CTE)--------------------------
with temp as (
select profit, if(profit>0,"Profit","Loss") as pnl from store)

select pnl,count(*) as number_of_orders
from temp
group by pnl;

# Calculate year wise profit margin ?

with year_wise_sales_data as (
select 
	year(order_date) as years , 
    round(sum(sales)) as total_sales ,
    round(sum(profit)) as total_profit
from store
group by years
order by years)

select * , round(total_profit / total_sales * 100,2) as profit_margin
from year_wise_sales_data;


# Find how many small, mid, high and very high value sales transactions are there in percentage ?

with temp as (
select case
			when sales < 50 then "Small"
            when sales < 200 then "Mid"
            when sales < 500 then "High"
            else "Very High"
		end as sales_category
from store)

select sales_category, count(*)/(select count(*) from store) * 100 as number_of_orders
from temp
group by sales_category
order by number_of_orders desc;


-- ------------------- Windows Functions -----------------------
select max(sales) over() from store;

select * , max(sales) over() from store;

select *,max(sales) over(partition by sub_category)
from store;

select region,sum(sales)
from store
group by region;

select * , sum(sales) over(partition by region)
from store;


select * from students;

select student_name, marks, rank() over(order by marks desc)
from students;

select * , rank() over(partition by department order by marks desc) as ranking
from students;

select student_name, marks, dense_rank() over(order by marks desc)
from students;

select student_name,marks, row_number() over()
from students;


select * , 
	rank() over(order by scholarship desc) as rank_func,
	dense_rank() over(order by scholarship desc) as dense_rank_func,
    ROW_NUMBER() over(order by scholarship desc) as row_number_func
    
from students;


# Find the top student from each deartment who has the first rank from his deartment  ?

with stud2 as (
select *, rank() over(partition by department order by marks desc) as ranking
from students)

select * 
from stud2
where ranking  =1 ;

-- create table
create table yearly_sales (
    year int,
    amount int
);

-- insert sample data
insert into yearly_sales
values
(2018, 4200),
(2019, 4450),
(2020, 3980),
(2021, 4625),
(2022, 4870),
(2023, 5150),
(2024, 5380),
(2025, 5560);

-- view data
select * 
from yearly_sales;


select *, lag(amount,2) over() as prv_year
from yearly_sales;

select * , lead(amount) over() as nxt_year
from yearly_sales;

# Change in sales amount from previous year 
with new as (
select year,amount as cur_year, lag(amount) over() as prv_year
from yearly_sales)

select * , cur_year - prv_year as changes
from new;





-- ------------------Views in MySQL ------------------------
/*A View in MySQL is a virtual table based on the resultset of a SQL query. It doesn't store data itself; instead, it stores the query that generates the data. When you query the view, MySQL runs the stored query and returns the result

Updatable View: A simple view (usually based on a single table) where you can use
INSERT, UPDATE, and DELETE.

Non-Updatable View: A complex view that uses things like sums, averages, or
grouping (GROUP BY). You can only use SELECT on it.
 */

create view  v1 as
select name,region,sales
from store
where region = "east" and sales >= 1000;

select * from v1;

insert into v1 values("rohan","east",5500);

select * from store;

create view  region_report as 
select region, sum(sales) as total_sales
from store
group by region;

select * from region_report;

insert into region_report values("random",500);



# Create a view to fetch a daily report of the last days total sales total profit and total quantity ?




-- --------------------Practice Questions -------------------
drop table students;
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
(101, 'arjun', 'male', 20, 'computer science', 3, 'indore', 91.00, 5000),
(102, 'priya', 'female', 19, 'computer science', 2, 'bhopal', 91.00, 8000),
(103, 'rohan', 'male', 21, 'mechanical', 5, 'indore', 72.50, 3000),
(104, 'neha', 'female', 20, 'civil', 4, 'ujjain', 91.00, 6000),
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


















