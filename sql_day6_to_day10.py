import sqlite3 as  sql

def see_all_data():
    lis=sql.connect('employees.db')
    d=lis.cursor()
    k="""SELECT * FROM employees 
    WHERE hire_date BETWEEN '2024-01-01' AND '2026-01-01'
    ;"""
    k=d.execute(k)
    lis.commit()
    for i in k:
        print(i)
see_all_data()


''' DAY 6 :

1️⃣ Employees earning more than average salary:

    SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

2️⃣ Employees earning less than average salary:

    SELECT * FROM employees
    WHERE salary < (SELECT AVG(salary) FROM employees);

3️⃣ Employees earning maximum salary:

    SELECT * FROM employees 
    WHERE salary = (SELECT MAX(salary) FROM employees);

4️⃣ Employees earning minimum salary:

    SELECT * FROM employees 
    WHERE salary = (SELECT MIN(salary) FROM employees);

5️⃣ Employees working in the same department as ‘Alice’:

    SELECT * FROM employees 
    WHERE department = (SELECT department FROM employees WHERE first_name = 'Alice');  

6️⃣ Employees earning more than HR department average salary:

    SELECT * FROM employees 
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = 'HR');

7️⃣ Employees hired before the earliest hire date of IT department:

    SELECT * FROM employees 
    WHERE hire_date < (SELECT MIN(hire_date) FROM employees WHERE department = 'IT');

8️⃣ Departments having employees earning more than overall average salary:

    SELECT department,SUM(salary) AS PER_DEP_SAL FROM employees 
    GROUP BY department 
    HAVING PER_DEP_SAL > (SELECT SUM(salary) FROM employees);  

9️⃣ Employees whose salary equals department maximum salary:

    SELECT * FROM employees E 
    WHERE salary = (SELECT MAX(salary) FROM employees WHERE department = E.department);

🔟 Employees whose salary equals department minimum salary:

    SELECT * FROM employees E 
    WHERE salary = (SELECT MIN(salary) FROM employees WHERE department = E.department);


DAY 7 :

1️⃣ Departments having average salary greater than overall average salary:

    SELECT department,AVG(salary) AS AVG_PER_DEP FROM employees 
    GROUP BY department
    HAVING AVG_PER_DEP > (SELECT AVG(salary) FROM employees);

2️⃣ Departments having total salary greater than Finance department:

    SELECT department,SUM(salary) AS TOTAL_PER_DEP FROM employees
    GROUP BY department
    HAVING TOTAL_PER_DEP > (SELECT SUM(salary) FROM employees WHERE department = 'Finance');

3️⃣ Departments having more employees than HR department:

    SELECT department,COUNT(*) AS NUM_OF_DEP FROM employees
    GROUP BY department 
    HAVING NUM_OF_DEP > (SELECT COUNT(*) FROM employees WHERE department = 'HR');

4️⃣ Departments where minimum salary is greater than overall minimum salary:

    SELECT department,MIN(salary) AS MIN_PER_DEP FROM employees
    GROUP BY department
    HAVING MIN_PER_DEP > (SELECT MIN(salary) FROM employees);

5️⃣ Departments where maximum salary is less than IT department maximum salary:

    SELECT department,MAX(salary) AS MAX_SAL_PER FROM employees
    GROUP BY department 
    HAVING MAX_SAL_PER < (SELECT MAX(salary) FROM employees WHERE department = 'IT');

6️⃣ Locations having more than average number of employees:

    SELECT location, COUNT(*) AS EMP_PER_LOC FROM employees
    GROUP BY location
    HAVING EMP_PER_LOC > (SELECT AVG(CNT) 
    FROM (SELECT COUNT(*) AS CNT FROM employees GROUP BY location ) x );

7️⃣ Departments with at least 2 employees:

    SELECT department,COUNT(*) AS PER_DEP_EMP FROM employees
    GROUP BY department
    HAVING PER_DEP_EMP >= 2;

8️⃣ Locations having total salary greater than London location:

    SELECT location,SUM(salary) AS TOT_PER_LOC FROM employees
    GROUP BY location 
    HAVING TOT_PER_LOC > (SELECT SUM(salary) FROM employees WHERE location = 'London');

9️⃣ Departments having highest average salary:

    SELECT department,AVG(salary) AS AVG_PER_DEP  FROM employees 
    GROUP BY department ORDER BY AVG_PER_DEP DESC LIMIT 1;

🔟 Departments having lowest average salary:

    SELECT department,AVG(salary) AS MIN_PER_DEP FROM employees 
    GROUP BY department ORDER BY MIN_PER_DEP ASC LIMIT 1; 


DAY 8 :

1️⃣ Find employees whose salary is greater than ALL salaries in the HR department:

   SELECT * FROM employees
   WHERE salary > ALL (SELECT salary FROM employees WHERE department ='HR');

2️⃣ Find employees whose salary is greater than ANY salary in the Sales department:

    SELECT * FROM employees 
    WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales');

3️⃣ Find employees whose salary matches the minimum salary of any department:

    SELECT * FROM employees 
    WHERE salary = ANY (SELECT MIN(salary) FROM employees GROUP BY department);

4️⃣ Find employees hired earlier than the oldest employee in their own department:

    SELECT * FROM employees e 
    WHERE hire_date < (SELECT MIN(hire_date) FROM employees WHERE department = e.department);

5️⃣ Find departments whose maximum salary is greater than the overall average salary:

    SELECT department,MAX(salary) AS MAX_PER_DEP FROM employees
    GROUP BY department
    HAVING MAX(salary) > (SELECT AVG(salary) FROM employees); 

6️⃣ Find locations where average salary is higher than IT department average salary:

    SELECT location,AVG(salary) FROM employees
    GROUP BY location
    HAVING AVG(salary) > (SELECT AVG(salary) FROM employees WHERE department = 'IT'); 

7️⃣ Find employees who work in departments that have more than 3 employees:

    SELECT * FROM employees 
    WHERE department IN (SELECT department FROM employees GROUP BY department HAVING COUNT(*) > 3);

8️⃣ Find employees who earn more than the average salary of their own location:

    SELECT * FROM employees e
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE location = e.location);

9️⃣ Find departments that have at least one employee earning more than 100,000:

    SELECT department,MAX(salary) FROM employees
    GROUP BY department
    HAVING MAX(salary)>100000 ;


🔟 Find employees who do not work in any department that has high earners (salary > 90,000):

    SELECT * FROM employees 
    WHERE department NOT IN 
    (SELECT department FROM employees WHERE salary>90000);

DAY 9 :

1️⃣ Get employee name along with their department name:

    SELECT first_name,department FROM employees;

2️⃣ Get employees earning more than 70,000 with their department:

    SELECT first_name,department FROM employees WHERE salary>70000; 

3️⃣ Get employees whose salary is higher than the average salary of all employees:

    SELECT * FROM employees 
    WHERE salary > (SELECT AVG(salary) FROM employees);

4️⃣ Get employees hired in the last 2 years:

    SELECT * FROM employees 
    WHERE hire_date BETWEEN '2024-01-01' AND '2026-01-01';

5️⃣ Get employees whose first name starts with ‘A’ and salary > 60,000:

    SELECT * FROM employees 
    WHERE first_name LIKE 'A%' AND salary>60000;

6️⃣ Get top 3 highest paid employees:

    SELECT salary FROM employees 
    ORDER BY salary DESC LIMIT 3;

7️⃣ Find employees with salary equal to the minimum salary in their department:

    SELECT * FROM employees e 
    WHERE salary = (SELECT MIN(salary) FROM employees WHERE department=e.department);

8️⃣ Count employees in each department:

    SELECT department,COUNT(*) FROM employees 
    GROUP BY department;

9️⃣ Find the average salary per department:

    SELECT department,AVG(salary) FROM employees
    GROUP BY department


🔟 Find departments with more than 3 employees:

   SELECT department,COUNT(*) FROM employees 
   GROUP BY department
   HAVING COUNT(*)>3;


DAY 10 :

1️⃣ Find employees whose salary is greater than the average salary of all employees:

    SELECT * FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees);

2️⃣ Find employees whose salary is less than the average salary of their department:

    SELECT * FROM employees e 
    WHERE salary < (SELECT AVG(salary) FROM employees WHERE department = e.department);

3️⃣ Find employees earning the maximum salary in the company:

    SELECT * FROM employees 
    WHERE salary = (SELECT MAX(salary) FROM employees);

4️⃣ Find employees earning the minimum salary in each department:

    SELECT * FROM employees e
    WHERE salary = (SELECT MIN(salary) FROM employees WHERE department=e.department);

5️⃣ Find employees who work in the same department as Alice:

    SELECT * FROM employees 
    WHERE department = (SELECT department FROM employees WHERE first_name='Alice');

6️⃣ Find employees whose salary is greater than the average salary of the HR department:

    SELECT * FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE department='HR');

7️⃣ Find employees hired before the earliest hired employee in the IT department:

    SELECT * FROM employees 
    WHERE hire_date < (SELECT MIN(hire_date) FROM employees WHERE department = 'IT');

8️⃣ Find departments whose total salary is greater than the total salary of the Finance department:

    SELECT department,SUM(salary) AS TOT_PER FROM employees 
    GROUP BY department
    HAVING TOT_PER > (SELECT SUM(salary) FROM employees WHERE department='Finance');

9️⃣ Find employees whose salary is equal to the maximum salary of their department:

    SELECT * FROM employees e
    WHERE salary = (SELECT MAX(salary) FROM employees WHERE department = e.department);

🔟 Find employees whose salary is equal to the minimum salary of their department:

    SELECT * FROM employees e
    WHERE salary = (SELECT MIN(salary) FROM employees WHERE department=e.department); 

'''