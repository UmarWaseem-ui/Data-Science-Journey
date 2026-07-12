# Day 2 - SQL JOINs

## Objective

To understand how SQL JOINs combine data from multiple tables based on related columns and learn when to use different types of JOIN operations in database queries.

---

## Topics Covered

### INNER JOIN

* Combines records that have matching values in both tables
* Returns only the common data between related tables

### LEFT JOIN

* Returns all records from the left table
* Returns matching records from the right table
* Displays `NULL` for unmatched records from the right table

### RIGHT JOIN

* Returns all records from the right table
* Returns matching records from the left table
* Displays `NULL` for unmatched records from the left table

### FULL OUTER JOIN (Concept)

* Returns all records from both tables
* Displays `NULL` where no matching record exists
* Useful for identifying unmatched records in either table

### SELF JOIN (Concept)

* Joins a table with itself
* Used to compare rows within the same table
* Commonly used for hierarchical data such as employees and managers

---

## SQL Commands Learned

* `INNER JOIN`
* `LEFT JOIN`
* `RIGHT JOIN`
* `FULL OUTER JOIN` *(Concept)*
* `SELF JOIN` *(Concept)*

---

## Files

* SQL_JoinS.sql
* Practice_Problems.sql

---

## Key Learnings

* SQL JOINs are used to retrieve related data from multiple tables.
* `INNER JOIN` returns only matching records from both tables.
* `LEFT JOIN` preserves all records from the left table, even when no match exists.
* `RIGHT JOIN` preserves all records from the right table.
* `FULL OUTER JOIN` combines all records from both tables, including unmatched ones.
* `SELF JOIN` allows a table to be queried against itself for comparisons and hierarchical relationships.

---

## Outcome

After completing Day 2, I can:

* Understand the purpose of SQL JOINs.
* Retrieve related information from multiple tables.
* Choose the appropriate JOIN based on the required result.
* Differentiate between INNER, LEFT, RIGHT, FULL OUTER, and SELF JOINs.
* Write SQL queries that combine data from multiple database tables.
