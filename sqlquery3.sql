Create Database EmployeeDB;

USE EmployeeDB;
GO
DROP TABLE employees;

CREATE TABLE employees(
id int identity(1,1) primary key,
name varchar(100) not null,
dept varchar(50) not null,
salary int not null
);
GO

INSERT INTO employees(name,dept,salary) Values('Rahul Sharma','Software Devloper',50000),
('Sonia Khatri','HR',90000),
('Zalak Gholi','Finance',80000),
('Amit Verma','Sales',48000),
('Vikas Yadav','IT Support',50000);

GO
SELECT *FROM employees;

USE EmployeeDB;
EXEC sp_rename 'employees.deptartment', 'dept', 'COLUMN';


USE EmployeeDB;
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'employees';

SELECT @@SERVERNAME;

USE EmployeeDB;

