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

describe customer;
select * from customer;

# delete a table
drop table customer;

# check the structure of a table
describe customer;

# to check the data in a table 
select * from customer;


# Create a table of sales with these columns -  						Order_id (A101), product, weight(5.67) , qty, sales?







# Create a table for library management system where there will be these table ?
# 1.Create a database Library
# 2.Create books_info table with - book_id, name, pages, writer, year
# 3.Create stock - book_id, total_books, issued, remaining


# Add a new column address in customer table
alter table customer add address varchar(100);

# Add a new column height in customer table


# Add a new column phone (bigint) in customer table


# Now change the data type of phone to varchar(10)? 
alter table customer modify column phone varchar(10);

# change column name sales to amount?
alter table customer change column sales amount int;

# delete column balance ?
alter table customer drop column balance;

# change the table name customer to new_customer?
alter table customer rename to new_customer;

# delete the table customer
drop table csutomer;

-- ------------------------------------------------------------
# DML

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

update emp
set age = 23, salary = 90000
where name = "sumit";

update emp
set age = 50;

select * from emp;

delete from emp
where name = "mohit";

truncate table emp;

delete from emp
where salary > 40000;

select * from emp;

describe emp;

show create table emp;

# DQL 

select * from store;


# select - use to show anything on screen

select 870 ;

select "hello world" as msg ;

select "Mohan" as name, 45 as age;

select name,city as location ,sales from store;

select name as customer_name from store;

# select with calculations
select name,sales,profit,sales-profit as cost from store;

###########  select with functions


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
    weekday(order_date)
from store;



select concat(name," ",state) from store;

select distinct category,sub_category from store;

select * from store;


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


select sub_category, sum(sales) as total_sales
from store
group by sub_category
having total_sales < 1000;

select * from emp;
select * from dep;

select *
from emp left join dep
on emp.depid = dep.depid
union all
select *
from emp right join dep
on emp.depid = dep.depid;

# Self Join
select * 
from emp  left join emp as manager
on emp.manager_id = manager.empid;



select * from emp;

select * 
from emp , dep
where emp.depid = dep.depid;


select * from emp
where salary > (select avg(salary) from emp) ;



# Find all the name of the customer who have made a transaction in east region and also made a transaction in other region also 
 
select * from store
where name in (select distinct name from store where region = "East");

select *
from (select * from store
where name in (select distinct name from store where region = "East") ) as newtable
where region != "East";

# find how many number of orders are profit and loss and what was there avg values?

;

select pnl , count(*) as count , avg(profit) as avg_profit
from (select profit, if(profit>0, "profit","Loss") as pnl from store) as newtable 
group by pnl;



with 
newtable as 
(select profit, if(profit>0, "profit","Loss") as pnl from store) ,

new2 as 
(select pnl , count(*) as count , avg(profit) as avg_profit from newtable group by pnl)

select *
from new2
where pnl = "loss";


select length(name),name
from store;












