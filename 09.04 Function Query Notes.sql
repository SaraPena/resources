USE sakila;
-- SQL functions are vectorized (applying a column to another vector)
select concat(address,",", district) as full_address from address;

select concat("Hello","\n", "World");

select concat(address, ", ",district) as full_address, district from address WHERE district not like '%berta';

select sin(`actor_id`) from actor;
select cos(actor_id) from actor;
select tan(actor_id) from actor;

select count(*) from actor;

select count(*) from salaries where salary > 63000 AND to_date > now();

select concat(first_name, " ", last_name) REGEXP '^a'as full_name from employees;

select concat(first_name, " ", last_name) as full_name from employees;

select SUBSTR(concat(first_name, " ", last_name),3,5) as full_name from employees;

select upper(name) from fruits;
select concat(upper(substr(name,1,1)), substr(name,2)) from fruits; -- *REVIEW* --

select replace(name, "cant", "ant") from fruits;

select sum(`id`) from fruits;

