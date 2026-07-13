# Day 3 - Advanced SQL

## Objective

To learn advanced SQL techniques for writing more efficient and powerful queries, including conditional logic, nested queries, Common Table Expressions (CTEs), and an introduction to Window Functions.

---

## Topics Covered

### CASE WHEN

* Applying conditional logic within SQL queries
* Creating custom values based on specified conditions
* Categorizing data dynamically

### Subqueries

* Writing queries inside other queries
* Using subqueries in `SELECT`, `FROM`, and `WHERE` clauses
* Simplifying complex data retrieval

### Common Table Expressions (CTEs)

* Creating temporary named result sets
* Improving query readability and organization
* Reusing query results within a single SQL statement

### Window Functions (Introduction)

* Understanding how window functions perform calculations across related rows without grouping data
* Comparing rows while preserving individual records

### ROW_NUMBER()

* Assigning a unique sequential number to each row
* Useful for pagination and ranking records

### RANK()

* Ranking records based on specified criteria
* Assigning the same rank to tied values while skipping subsequent ranks

### DENSE_RANK()

* Ranking records while assigning the same rank to tied values
* Maintaining consecutive ranking numbers without gaps

---

## SQL Commands Learned

* `CASE WHEN`
* Subqueries
* `WITH` (Common Table Expressions - CTEs)
* `ROW_NUMBER()`
* `RANK()`
* `DENSE_RANK()`

---

## Files

* SQL_CaseWhen.sql
* SQL_SubQueries.sql
* SQL_CTEs.sql
* SQL_WindowFunctions.sql
* Practice_Problems.sql

---

## Key Learnings

* `CASE WHEN` adds conditional logic directly within SQL queries.
* Subqueries allow complex problems to be solved by nesting queries.
* Common Table Expressions (CTEs) improve query readability and make complex SQL easier to manage.
* Window functions perform calculations across rows while keeping each row visible in the result set.
* `ROW_NUMBER()` assigns a unique number to every row.
* `RANK()` and `DENSE_RANK()` are used to rank records, with different behavior when duplicate values exist.

---

## Outcome

After completing Day 3, I can:

* Apply conditional logic using `CASE WHEN`
* Write and understand subqueries
* Use Common Table Expressions (CTEs) to simplify complex SQL queries
* Apply Window Functions for advanced data analysis
* Rank records using `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`
* Write advanced SQL queries for real-world data analysis and reporting
