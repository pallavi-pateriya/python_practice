*** SELECT ***
Reference Table: Employees
-----------------------------------------------------
EmpID	Name	Department	Salary	City	JoinDate
101	Aarav	IT	85000	Indore	2022-03-15
102	Diya	HR	55000	Bhopal	2021-07-10
103	Kabir	IT	92000	Indore	2020-11-01
104	Meera	Sales	60000	Mumbai	2023-01-20
105	Rohan	Sales	60000	Bhopal	2022-08-05
106	Ananya	HR	58000	Indore	2024-02-12
-----------------------------------------------------
1. Write a query to display the Name and City of all employees who work in the Sales department.
SELECT Name, City 
FROM Employees 
WHERE Department = 'Sales';

2. Write a query to get all details (*) of employees who live in Bhopal OR earn more than 80,000.
SELECT * 
FROM Employees 
WHERE City = 'Bhopal' OR Salary > 80000;

3. Sorting: Write a query to show the Name and JoinDate of all employees, sorted from the newest joiner to the oldest joiner.
SELECT Name, JoinDate 
FROM Employees 
ORDER BY JoinDate DESC;

4. Pattern Matching: Write a query to find the Name and Salary of employees whose name ends with the letter 'a'.
SELECT Name, Salary 
FROM Employees 
WHERE Name LIKE '%a';

5. Grouping & Counting: Write a query to count how many employees live in each City.
SELECT City, COUNT(City) AS Occurrence 
FROM Employees 
GROUP BY City;

6. Basic Filter: Write a query to get the Name and Salary of all employees who live in Indore.
SELECT Name, Salary FROM Employees WHERE City = 'Indore';

7. Multiple Conditions: Write a query to get all details (*) of employees who work in the IT department AND earn more than 90,000.
SELECT * FROM Employees WHERE Department = 'IT' AND Salary > 90000;

8. Sorting: Write a query to show the Name and Salary of all employees, sorted from the lowest salary to the highest salary.
SELECT Name, Salary FROM Employees ORDER BY Salary ASC;

9. Pattern Matching: Write a query to find the Name and Department of employees whose name starts with the letter 'A'.
SELECT Name, Department FROM Employees WHERE Name LIKE 'A%';

10. Grouping & Counting: Write a query to count how many employees work in each Department.
SELECT Department, COUNT(Department) AS C FROM Employees GROUP BY Department;

*** ORDER BY ***
Reference Table: Employees
__________________________________________________
EmpID	Name	Department	Salary	City  JoinDate
101	Aarav	IT	85000	Indore	2022-03-15
102	Diya	HR	55000	Bhopal	2021-07-10
103	Kabir	IT	92000	Indore	2020-11-01
104	Meera	Sales	60000	Mumbai	2023-01-20
105	Rohan	Sales	60000	Bhopal	2022-08-05
106	Ananya	HR	58000	Indore	2024-02-12
___________________________________________________

1. Alphabetical Sort: Write a query to get all details (*) of employees, sorted alphabetically by their Name from A to Z.
SELECT * FROM Employees ORDER BY Name;

2. Filter + Sort (WHERE + ORDER BY): Write a query to get the Name and Salary of employees who live in Indore, sorted from the highest salary to the lowest.
SELECT Name, Salary 
FROM Employees 
WHERE City = 'Indore' 
ORDER BY Salary DESC;

3. Multi-Column Sort (Tie-Breaker): Write a query to show Name, Department, and Salary for all employees. Sort first by Department (A to Z), and if two employees are in the same department, sort them by Salary (highest to lowest).
SELECT Name, Department, Salary 
FROM Employees 
ORDER BY Department, Salary DESC;

4. Sorting by a Calculated Column: Write a query to display Name and their annual bonus calculated as Salary * 0.10 AS Bonus, sorted from the largest Bonus to the smallest.
SELECT Name, Salary * 0.10 AS Bonus 
FROM Employees 
ORDER BY Bonus DESC;

5. Top N Records (ORDER BY + LIMIT): Write a query to find the Name and JoinDate of the 2 earliest (oldest) employees who joined the company.
SELECT Name, JoinDate 
FROM Employees 
ORDER BY JoinDate 
LIMIT 2;

*** DISTINCT ***

1. Single-Column DISTINCT: Write a query to get a list of all unique City names where employees live (no duplicates).
SELECT DISTINCT City FROM employees;

2. DISTINCT + WHERE: Write a query to find all unique Department names that exist in Indore.
SELECT DISTINCT DEPARTMENT FROM employees WHERE City = 'Indore';

3. DISTINCT + ORDER BY: Write a query to get all unique Salary amounts across the company, sorted from highest to lowest.
SELECT DISTINCT Salary FROM employees ORDER BY Salary DESC;

4. Multi-Column DISTINCT: Write a query to get every unique combination of Department and City (for example, IT - Indore appears twice in the table, so it should only show up once in your result). (Hint: Put DISTINCT right after SELECT before both column names.)
SELECT DISTINCT Department, City FROM employees ;

5. Counting Unique Values (COUNT(DISTINCT ...)): Write a query to return a single number showing how many unique cities the company operates in. (Hint: Put DISTINCT City inside the COUNT() parentheses.)
SELECT Count(DISTINCT City) FROM employees;

*** LIMIT AND OFFSET ***
1. Basic LIMIT: Write a query to display all details (*) of only the first 3 rows from the Employees table.
SELECT * FROM employees LIMIT 3;

2. Top N with Sorting: Write a query to get the Name and Salary of the top 2 highest-paid employees.
SELECT Name, Salary FROM employees ORDER BY Salary DESC LIMIT 2;

3. Finding the Nth Highest Value (LIMIT + OFFSET): Write a query to find the Name and Salary of only the 3rd highest-paid employee.
SELECT Name, Salary FROM employees ORDER BY Salary DESC LIMIT 1 OFFSET 2;

4. Pagination Simulation: Imagine a web app shows 2 employees per page, sorted alphabetically by Name (A to Z). Write a query to fetch Page 2 
SELECT * FROM employees ORDER BY Name  LIMIT 2 OFFSET 2;

5. Filtering + Skipping (WHERE + ORDER BY + LIMIT + OFFSET): Among employees who live in Indore, find the Name and JoinDate of the 2nd newest joiner 
SELECT Name, JoinDate FROM employees WHERE City = 'Indore' ORDER BY JoinDate DESC LIMIT 1 OFFSET 1;

*** OFFSET AND FETCH ***
1. Basic Top-N: Write a query to get the 3 most expensive products.
SELECT product_name FROM Product ORDER BY price DESC FETCH FIRST 3 ROWS ONLY;

2. Pagination: Suppose a webpage displays 2 products per page sorted alphabetically by product_name. Write a query to fetch the products for Page 3.
SELECT product_name FROM Product ORDER BY product_name OFFSET 4 ROWS FETCH NEXT 2 ROWS ONLY;

3. Handling Ties: Write a query to get the 2 cheapest products, making sure to include any other products tied for the second-lowest price.,
SELECT product_name FROM Product ORDER BY price FETCH FIRST 2 ROWS WITH TIES;

4. Filtering + FETCH: Write a query to find the single cheapest product in the 'Electronics' category.
SELECT product_name FROM Product WHERE category = 'Electronics' ORDER BY price FETCH FIRST 1 ROW ONLY;

5. Interview Classic: Write a query to find the 3rd highest distinct price from the Products table.
SELECT DISTINCT price FROM Product ORDER BY price DESC OFFSET 2 ROW FETCH NEXT 1 ROW ONLY;

*** WHERE CLAUSE ***

1. Basic Comparison: Write a query to find the name and salary of all employees who earn more than 60,000.
SELECT name, salary FROM employees WHERE salary > 60000;

2. Multiple Conditions (AND / OR): Write a query to find all details of employees who work in the IT department AND have a salary greater than 80,000.
SELECT * FROM employees WHERE department = 'IT' AND salary > 80000;

3. Matching a List (IN): Write a query to find the name and department of employees who work in either IT, Finance, or HR.
SELECT name, department FROM employees WHERE department IN('IT', 'Finance', 'HR');

4. Range Filtering (BETWEEN): Write a query to find the name and salary of employees whose salary is between 50,000 and 85,000 (inclusive).
SELECT name, salary FROM employees WHERE salary between 50000 and 85000;

5. Pattern Matching (LIKE): Write a query to find all employees whose name starts with the letter 'A'.
SELECT * FROM employees where name LIKE 'A%';

6. Handling Missing Values (IS NULL): Write a query to find the name of employees who do not receive a bonus (i.e., bonus is NULL).
SELECT name FROM employees WHERE bonus is NULL;

*** AND ***
--Write a query to find all employees in the 'IT' department who earn more than 60,000.
SELECT name FROM employees WHERE department = 'IT' AND salary > 60000;

--If a row has country = 'India' and discount_code = NULL, will it be returned by the query below?
SELECT * FROM Customers WHERE country = 'India' AND discount_code is NULL;

--Write a query to fetch all customers from the 'USA' who are older than 25.
SELECT * FROM Customers WHERE country = 'USA' AND age > 25;

--Write a query to find all customers whose first_name is 'John' and who live in the 'UK'.
SELECT * FROM Customers WHERE first_name = 'John' AND country = 'UK' 

--Write a query to find all customers whose age is at least 22 and at most 28.
SELECT * FROM Customers WHERE age >= 22 AND age <= 28;

--Write a query to find customers who live in 'USA' or 'UK' and have the last_name 'Doe'.
SELECT * FROM Customers WHERE (country = 'USA' OR country = 'UK') AND last_name = 'Doe';

--Write a query to find customers whose last_name starts with 'R' and whose age is not 22.
SELECT * FROM Customers WHERE last_name LIKE 'R%' AND age != 22; 

*** BETWEEN AND NOT BETWEEN ***
1. Basic Age Range: Write a query to find all customers whose age is between 22 and 28 (inclusive).
SELECT * FROM Customers WHERE age BETWEEN 22 AND 28;

2. ID Range + Country: Write a query to fetch all customers with a customer_id between 1 and 4 and who live in the 'UK'.
SELECT * FROM Customers WHERE customer_id BETWEEN 1 AND 4 AND country = 'UK';

3. Alphabetical Range: Write a query to find all customers whose first_name starts with letters between 'A' and 'K' (hint: BETWEEN 'A' AND 'L', or use first_name BETWEEN 'B' AND 'J').
SELECT * FROM Customers WHERE first_name BETWEEN 'A' AND 'K';

Part 2: NOT BETWEEN Challenges

4. Outside Age Range: Write a query to find all customers whose age is not between 23 and 30.
SELECT * FROM Customers WHERE age NOT  BETWEEN 23 AND 30;

5. Outside ID Range: Write a query to fetch all customers whose customer_id is not between 2 and 4.
SELECT * FROM Customers WHERE customer_id NOT BETWEEN 2 AND 4;

6. Combined Filter: Write a query to find all customers from the 'USA' whose age is not between 25 and 35.
SELECT * FROM Customers WHERE Country = 'USA' AND  age NOT BETWEEN 25 AND 35;

*** IN ***
1. Multiple Countries: Write a query to find all customers who live in 'USA' or 'UAE' using IN.
SELECT * FROM Customers WHERE country IN ('USA', 'UAE');

2. Specific IDs: Write a query to fetch all customers whose customer_id is 1, 3, or 5.
SELECT * FROM Customers WHERE customer_id IN (1, 3, 5);

3. Specific Ages + Country: Write a query to find all customers whose age is 22 or 28 and who live in 'USA' or 'UK'.
SELECT * FROM Customers WHERE Country IN ('USA', 'UK') AND age IN (22, 28);

4. Last Names List: Write a query to find all customers whose last_name is either 'Doe' or 'Luna'.
SELECT * FROM Customers WHERE last_name IN ('Doe', 'Luna');

5. First Names + Age Filter: Write a query to find customers whose first_name is 'John', 'David', or 'Betty' and who are older than 24.
SELECT * FROM Customers WHERE first_name IN ('John', 'David', 'Betty') AND age > 24;

 *** NOT IN ***
1. Exclude Countries: Write a query to find all customers who do not live in 'USA' or 'UK'.
SELECT * FROM Customers WHERE country NOT IN ('USA', 'UK');

2. Exclude IDs: Write a query to fetch all customers whose customer_id is not 2 or 4.
SELECT * FROM Customers WHERE customer_id NOT IN (2, 4);

3. Exclude First Names: Write a query to find all customers whose first_name is not 'John' or 'Robert'.
SELECT * FROM Customers WHERE first_name NOT IN ('John', 'Robert');

4. Exclude Ages + Country Filter: Write a query to find customers from the 'UK' whose age is not 22 or 30.
SELECT * FROM Customers WHERE age NOT IN (22, 30) AND country = 'UK';

5. Combined IN and NOT IN: Write a query to find customers whose country is 'USA' or 'UK' and whose last_name is not 'Doe' or 'Reinhardt'.

SELECT * FROM Customers WHERE last_name NOT IN ('Doe', 'Reinhardt') AND country IN ('USA', 'UK');

*** LIKE ***
1. Starts With (%): Write a query to find all customers whose first_name starts with 'J'.
SELECT * FROM Customers WHERE first_name LIKE 'J%';

2. Ends With (%): Write a query to find all customers whose last_name ends with 'n' (e.g., Robinson).
SELECT * FROM Customers WHERE last_name LIKE '%n';

3. Contains Substring (%...%): Write a query to find all customers whose last_name contains 'in' anywhere in the name.
SELECT * FROM Customers WHERE last_name LIKE '%in%';

4. Exact Character Length (_): Write a query to find all customers whose first_name is exactly 4 letters long (hint: use four underscores ____).
SELECT * FROM Customers WHERE first_name LIKE '____';

5. Specific Letter Position (_ + %): Write a query to find all customers whose last_name has 'o' as the second letter (e.g., Doe, Robinson).
SELECT * FROM Customers WHERE last_name LIKE '_o%';

*** NOT LIKE ***
1. Does Not Start With: Write a query to find all customers whose first_name does not start with 'J'.
SELECT * FROM Customers WHERE first_name NOT LIKE 'J%';

2. Does Not End With: Write a query to find all customers whose last_name does not end with 'e'.
SELECT * FROM Customers WHERE last_name NOT LIKE '%e';

3. Does Not Contain: Write a query to find all customers whose country does not contain 'A' (note: in SQLite/MySQL LIKE is case-insensitive by default, while in PostgreSQL ILIKE is case-insensitive—use 'A' or 'a').
SELECT * FROM Customers WHERE country NOT LIKE '%A%';

4. Exclude Exact Length: Write a query to find all customers whose last_name is not 3 letters long.
SELECT * FROM Customers WHERE last_name NOT LIKE '___';

5. Combined LIKE and NOT LIKE: Write a query to find all customers whose country starts with 'U' and whose first_name does not end with 'n'.*/
SELECT * FROM Customers WHERE first_name NOT LIKE '%n' AND country LIKE 'U%';

______JOIN________
*** INNER JOIN ***
1. Write a query to display each customer's first_name, last_name, and the item they ordered (only for customers who have placed an order).
SELECT C.first_name, C.last_name, O.item FROM Customers C INNER JOIN Orders O on (C.customer_id = O.customer_id);

2. INNER JOIN with WHERE (Country Filter)
Write a query to show the first_name, country, item, and amount for all orders placed by customers from the 'UK'.
SELECT C.first_name, C.country, O.item, O.amount FROM Customers C INNER JOIN Orders O on (C.customer_id = O.customer_id) WHERE C.country = 'UK'

3. INNER JOIN with Amount & Age Conditions
Write a query to find the first_name, age, and item where the order amount is greater than 350 and the customer's age is under 30.
SELECT C.first_name, C.age, O.item FROM Customers C INNER JOIN Orders O on (C.customer_id = O.customer_id) WHERE O.amount > 350 AND C.age < 30;
4. INNER JOIN with LIKE / IN
Write a query to fetch the order_id, first_name, and item for orders where the item is either 'Keyboard' or 'Mouse' and the customer's first_name starts with 'J'.
SELECT O.order_id, C.first_name, O.item FROM Customers C INNER JOIN Orders O on (C.customer_id = O.customer_id) WHERE O.item IN ('Keyboard', 'Mouse') AND C.first_name LIKE 'J%';

5. INNER JOIN + GROUP BY (Bonus Challenge)
Write a query to display each customer's first_name and the total amount (SUM(amount)) they have spent across all their orders.*/
SELECT C.first_name, SUM(O.amount) AS total_spent FROM Customers C INNER JOIN Orders O on (C.customer_id = O.customer_id) GROUP BY O.customer_id;

6. List the first_name, last_name, and item for every order that has a matching customer.
SELECT C.first_name, C.last_name, O.item FROM Customers C INNER JOIN Orders O ON (C.customer_id = O.customer_id);

7. Find all orders with an amount greater than 300, showing order_id, item, amount, and the customer's country.
SELECT O.order_id, O.item, O.amount, C.country FROM Customers C INNER JOIN Orders O ON C.customer_id = O.customer_id WHERE O.amount > 300;

8. Display first_name, item, and status by joining Customers, Orders, and Shippings on their customer ID columns.
SELECT C.first_name, O.item, S.status 
FROM Customers C 
INNER JOIN Orders O ON C.customer_id = O.customer_id 
INNER JOIN Shippings S ON C.customer_id = S.customer;

9. Retrieve the first_name, last_name, and order_id for customers from the UK who have placed an order.
SELECT C.first_name, C.last_name, O.order_id FROM Customers C INNER JOIN Orders O ON C.customer_id = O.customer_id WHERE country = 'UK';

10. List each customer's first_name, age, and status for rows where a matching record exists in Shippings.
SELECT C.first_name, C.age, S.status FROM Customers C INNER JOIN Shippings S ON C.customer_id = S.customer;






