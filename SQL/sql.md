A database is a structured collection of data stored on a computer. It is a powerful tool for storing and organizing data efficiently.

There are common two type of database:
1. RDBMS- This is the most common database type, organizing data into table with rows and columns. The popular RDBMS are Postgrsql, MySql, Oracle database.
2. Documnet Databse (NoSql database)- These types of databse stores data as documents. The popular document databases are mongodb, databricks.

TO interact with data in rdbms, you need to use sql.

Overview of SQL
SQL Stand for structured query language. It is an standard language for interacting with RDBMS. It allows you to:
* Create and maintain database structure such as tables.
* Insert update and delete data.
* Retrieve data from tables.

SQL consists of three main parts:
1. Data definition language(DDL) deals with database structure creation and modification. For example CREATE TABLE, ALTER TABLE, DROP TABLE.
Behaviour: DDL commands are auto committed. Once executed the changes are permanent and can not be undone using standard ROLLBACK.
Core Commands: 
* Create builds a new database object such as a table or database.
* Alter modifies an existing object's structure, such as adding column or changing datatype
* Drop permanently deletes an entire object along with all its data and structure.
* TRUNCATE removes all rows from a table instantly while preserving the table's column structure for future use.
* RENAME changes the name of an existing database object.

2. Data manipulation language(DML) DML commands manage and modify the actual records (rows) stored inside database tables. Once DDL builds the container, DML fills and updates it. it provides statements to query data, such as the SELECT statement and modify data like INSERT, UPDATE, and DELETE statements.
Behavior: DML operations are not auto-committed by default inside explicit transactions. You can undo changes with ROLLBACK or save them permanently with COMMIT
Core Commands.
INSERT adds new rows of data into a table.
UPDATE modifies existing values in one or more rows, usually filtered by a WHERE clause.
DELETE removes specific rows from a table based on a condition (or all rows if no condition is specified, though slower than TRUNCATE because it logs each row deletion).
SELECT retrieves data from one or more tables.

3. Data control language(DCL) includes statements, working with user authorization and security, such as GRANT and REVOKE statements. DCL commands manage security, privileges, and access control across the database. Database administrators (DBAs) use DCL to decide which users or roles can read, modify, or administer specific objects.
Behavior: Like DDL, DCL statements generally take effect immediately and are auto-committed in most database engines.
Core Commands.
GRANT gives specific privileges (e.g., SELECT, INSERT, ALL) on a database object to a user or role.
REVOKE withdraws previously granted privileges from a user or role

The core of an RDBMS is tables. Tables allow you to organize data in rows and columns:
Columns: represent specific fields
Rows: stores individual records.

SQL is a declarative language. It means you tell the database what you want, not how to get it. This feature makes SQL very easy to learn compared to other programming languages.

Most SQL statements follow a pattern:

Verb (Action): is the action you want the database to do, such as SELECT, INSERT, UPDATE, and DELETE.
Subject (Target): is the database object you work with, such as a table.
Condition (Filter): choose which data you’re interested in.

Comments 
Comments are notes you add to your SQL code to explain why it does a specific task.
The database ignores comments, but they’re helpful for you and others to understand and troubleshoot later.
SQL supports two types of comments:
Single-line comments start with two hyphens (--) and is followed by a comment.
Multi-line comments start with /* and end with */. The text between these is a comment.


SELECT Statement:-
The SELECT statement allows you to retrieve data from one or more tables.
Here’s the basic syntax of the SELECT statement that retrieves data from a single table:
SELECT
  select_list
FROM
  table_name;

In this syntax:

First, specify a comma-separated list of columns from the table you want to retrieve data in the SELECT clause.
Then, provide the table name in the FROM clause.
When evaluating the SELECT statement, the database system evaluates the FROM clause first and then the SELECT clause.
The semicolon (;) is not part of a query. The database server uses the semicolon to separate two SQL statements.
For example, if you execute two SELECT statements, you need to separate them using a semicolon (;). 
A column alias is a temporary name you assign to a column during the execution of a query. 
Here’s the syntax for using a column alias:
|expression AS column_alias|
In this syntax, the AS keyword is optional. Therefore, you can omit it to make the query more concise:
___expression column_alias___

Summary 
Use the SELECT statement to retrieve data from a table.
Use the SELECT star to retrieve data from all columns of a table.
A column alias is a temporary name of a column in a query.
1. Always put text values in 'single quotes'.
2. Combine WHERE conditions with AND / OR (never commas).
3. Use ORDER BY ColumnName DESC to sort.
4. Use LIKE '%pattern' for wildcard text searches.
5. Pair COUNT() with GROUP BY when selecting another column.

ORDER BY:
The ORDER BY is an optional clause of the SELECT statement. The ORDER BY clause allows you to sort the result set by one or more sort expressions in ascending and/or descending order.
The ORDER BY clause uses the ASC option by default. It means that the ORDER BY clause sorts the rows in the result set by the sort_expression in ascending order if you don’t specify either ASC or DESC.
Note that if you don’t specify the ORDER BY clause, the SELECT statement will not sort the result set. It means the rows in the result set don’t have a specific order.
The database system evaluates the SELECT statement with the ORDER BY clause in the following order:
FROM
SELECT
ORDER BY

Summary 
Use the ORDER BY clause to sort rows in a result set.
Use the ASC option to sort rows in ascending order and DESC option to sort rows in descending order.
Use NULLS FIRST to place NULLs before and NULLS LAST to place NULLs after other non-NULL values.

DISTINCT Operator:
To select the distinct values from a column of a table, you use the DISTINCT operator in the SELECT clause as follows:
SELECT DISTINCT
  column1
FROM
  table_name;
In this syntax, the SELECT statement returns a result set that contains unique values from the column1 of the table.
Use DISTINCT operator in the SELECT clause to select unique values from one or more columns of a table.
Always place DISTINCT immediately after SELECT (never SELECT Department, DISTINCT City—that throws a syntax error because DISTINCT deduplicates the entire row, not a single column in the middle).

LIMIT:-
To limit the number of rows returned by a SELECT statement, you use the LIMIT and OFFSET clauses.

Here’s the syntax of LIMIT & OFFSET clauses:

SELECT
  column_list
FROM
  table1
ORDER BY
  column_list
LIMIT
  row_count
OFFSET
  row_to_skip;
In this syntax:

The LIMIT row_count determines the number of rows (row_count) returned by the query.
The OFFSET row_to_skip clause skips the row_to_skip rows before beginning to return the rows.
The OFFSET clause is optional. If you omit it, the query will return the row_count rows from the first row returned by the SELECT clause.
When you use the LIMIT clause, it is important to use an ORDER BY clause to ensure the order of rows in the result set.
Suppose you have to get employees who have the 2nd highest salary in the company. To do so, you use the LIMIT OFFSET clauses as follows.

SELECT
  employee_id,
  first_name,
  last_name,
  salary
FROM
  employees
ORDER BY
  salary DESC
LIMIT
  1
OFFSET
  1;
Summary 
Use the LIMIT clause to limit the number of rows returned by a query.
Use the OFFSET clause to skip some rows before returning the number of rows specified by the LIMIT clause.

FETCH:-
The OFFSET FETCH clause allows you to skip the first N rows in a result set before starting to return rows.
Here’s the syntax of the FETCH clause:
OFFSET rows_to_skip { ROW | ROWS }
FETCH { FIRST | NEXT } [ row_count ] { ROW | ROWS } ONLY
How the query works:
First, the ORDER BY clause sorts the employees by first and last names in alphabetical order.
Second, the OFFSET clause skips the first five rows.
Third, the FETCH clause returns the next five rows.
Summary 
Use the FETCH clause to limit the number of rows returned by a query.
Use the OFFSET clause to skip N rows before starting to return the number of rows specified in the FETCH clause.


