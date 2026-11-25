SELECT

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

ORDER BY :-
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

DISTINCT:-

1. Single-Column DISTINCT: Write a query to get a list of all unique City names where employees live (no duplicates).
SELECT DISTINCT City FROM employees

2. DISTINCT + WHERE: Write a query to find all unique Department names that exist in Indore.
SELECT DISTINCT DEPARTMENT FROM employees WHERE City = 'Indore'
3. DISTINCT + ORDER BY: Write a query to get all unique Salary amounts across the company, sorted from highest to lowest.
SELECT DISTINCT Salary FROM employees ORDER BY Salary DESC;

4. Multi-Column DISTINCT: Write a query to get every unique combination of Department and City (for example, IT - Indore appears twice in the table, so it should only show up once in your result). (Hint: Put DISTINCT right after SELECT before both column names.)
SELECT DISTINCT Department, City FROM employees 

5. Counting Unique Values (COUNT(DISTINCT ...)): Write a query to return a single number showing how many unique cities the company operates in. (Hint: Put DISTINCT City inside the COUNT() parentheses.)
SELECT Count(DISTINCT City) FROM employees

LIMIT AND OFFSET:-
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

OFFSET AND FETCH 
1. Basic Top-N: Write a query to get the 3 most expensive products.
SELECT product_name FROM Product ORDER BY price DESC FETCH FIRST 3 ROWS ONLY

2. Pagination: Suppose a webpage displays 2 products per page sorted alphabetically by product_name. Write a query to fetch the products for Page 3.
SELECT product_name FROM Product ORDER BY product_name OFFSET 4 ROWS FETCH NEXT 2 ROWS ONLY

3. Handling Ties: Write a query to get the 2 cheapest products, making sure to include any other products tied for the second-lowest price.,
SELECT product_name FROM Product ORDER BY price FETCH FIRST 2 ROWS WITH TIES

4. Filtering + FETCH: Write a query to find the single cheapest product in the 'Electronics' category.
SELECT product_name FROM Product WHERE category = 'Electronics' ORDER BY price FETCH FIRST 1 ROW ONLY;

5. Interview Classic: Write a query to find the 3rd highest distinct price from the Products table.
SELECT DISTINCT price FROM Product ORDER BY price DESC OFFSET 2 ROW FETCH NEXT 1 ROW ONLY;


