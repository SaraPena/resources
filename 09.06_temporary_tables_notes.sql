USE bayes_826;

CREATE TEMPORARY TABLE employee_salary AS
	SELECT first_name, last_name, salary
	FROM employees.employees
	JOIN employees.salaries using(emp_no);
	
select * 
from employee_salary;

-- table creation syntax (for permanent tables, remove the temporary keyword)
CREATE TEMPORARY TABLE captains(
	name VARCHAR(256) not null,
	ship VARCHAR(256) not null
	);
	
-- How to add new records to a table
INSERT INTO captains (name,ship) VALUES ("Captain Ahab", "Pequad");

select * FROM captains;

INSERT INTO captains (name, ship) VALUES
	("Jean Luc Piccard", "USS Starship Enterprise NCC1701D"),
	("James Tiberius Kirk", "USS Starship Enterprise NCCI701A");
	
SELECT * FROM captains;

-- Using the select to double check what you're going to delete
-- IF you ever need to delete a row or rows create the select statement first.

SELECT * FROM captains WHERE name = 'Captain Ahab';

DELETE FROM captains WHERE name = 'Captain Ahab';

SELECT * FROM captains;

DELETE from captains;

CREATE TEMPORARY TABLE fruits (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL, 
	primary key(id)
);

INSERT INTO fruits (name) VALUES("Mango");
INSERT INTO fruits (name) VALUES("Kiwi");

INSERT INTO fruits (name) VALUES
	("Tangerine"),
	("Gala Apple"),
	("Banana");
	
SELECT * from fruits;



-- ADDING COLUMNS

ALTER TABLE fruits ADD quantity INT UNSIGNED;

ALTER TABLE fruits DROP COLUMN id;

SELECT * from fruits;


-- UPDATE SYNTAX - for an entire column

UPDATE fruits
SET quantity = 10;

SELECT * from fruits;

-- How to update a specific row's column value

UPDATE fruits
SET quantity = quantity + 20
WHERE name = "Kiwi";

UPDATE fruits
SET quantity =+ 20
WHERE name = "Kiwi";

select * from fruits;


UPDATE fruits
SET name = "Red Apple"
WHERE name = 'Gala Apple';

select * from fruits;


