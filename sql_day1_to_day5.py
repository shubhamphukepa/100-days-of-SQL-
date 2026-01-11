import sqlite3 as sql
def query_execute(query):
   lis=sql.connect('employees.db')
   lis1=lis.cursor()
   lis1.execute(query)
   lis.commit()
   lis.close()
   print('operation perform  successfully')
def table_emp1():
    k=''' CREATE TABLE employees (
          employee_id INTEGER  PRIMARY KEY,
          first_name VARCHAR(30),
          last_name VARCHAR(30),
          department VARCHAR(30),
          job_id VARCHAR(30),
          salary INTEGEE,
          hire_date DATE,
          location VARCHAR(30)
          )
          '''
    query_execute(k)
def insert_table1():
    k='''INSERT INTO employees VALUES
    (1,'Alice','Brown','IT','Developer', 0,'2018-06-10','New York'),
    (3,'Charlie','Davis','IT','Developer',80000,'2020-01-20','London'),
    (4,'David','Wilson','Finance','Analyst',50000,'2017-09-12','Toronto'),
    (5,'Eva','Johnson','Marketing','Executive',65000,'2021-02-05','London'),
    (6,'Frank','Miller','Sales','Salesman',55000,'2019-11-25','New York'),
    (7,'Grace','Taylor','HR','Recruiter',58000,'2020-08-14','Toronto'),
    (8,'Helen','Anderson','Sales','Manager',90000,'2016-04-30','London'),
    (9,'Ian','Thomas','IT','Manager',95000,'2015-12-01','New York'),
    (10,'John','Moore','Finance','Clerk',45000,'2022-07-19','London');'''
    query_execute(k)

          
def table2_dep():
    k=f''' CREATE TABLE departments1 (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL)'''
    query_execute(k)
def insert_table2():
    department_id=int(input('enter Department id  '))
    department_name=str(input('enter Department name '))
    k=f'''INSERT INTO departments1 VALUES({department_id},'{department_name}')'''
    query_execute(k)
def table_3():
    k='''CREATE TABLE location1 (
        location_id INTEGER,
        location_name  VARCHAR(50)
        )'''
    query_execute(k)
def insert_3():    
    location_id=int(input('enter the location_id'))     
    location_name=str(input('enter the locationd'))
    K=f"INSERT INTO location1  VALUES({location_id},'{location_name}')"
    query_execute(K)
def Alter_table():
    k=" select Name,Location from employees inner join departments on employees.Department=departments.Departme"
    query_execute(k)
def update_record():
    Department=str(input('enter live location  '))
    EmpID=int(input('enter EmpID  '))
    k=f"UPDATE employees  SET Department='{Department}' WHERE EmpID={EmpID}"   
    query_execute(k)     
def see_all_data():
    lis=sql.connect('employees.db')
    d=lis.cursor()
    k="""  SELECT department,SUM(salary) AS total_sal FROM employees GROUP BY department HAVING total_sal>200000;"""
    k=d.execute(k)
    lis.commit()
    for i in k:
        print(i)
see_all_data()



''' DAY1 :
1️⃣ Display all records from the employees table :
    
    SELECT * FROM employees;

2️⃣ Display only first_name and salary from employees:
    
    SELECT first_name,salary FROM employees;

3️⃣ Display employees who belong to the Sales department:

    SELECT * FROM employees WHERE department='Sales';

4️⃣ Display employees whose salary is greater than 50,000:

    SELECT * FROM employees WHERE salary>50000;

5️⃣ Display employees who work in Marketing or HR:

    SELECT * FROM employees WHERE department='Marketing' or department='HR';

6️⃣ Display employees who do not belong to Finance:
    
    SELECT * FROM employees WHERE department != 'Finance';

7️⃣ Display employees ordered by last_name ascending:
   
    SELECT * FROM employees ORDER BY last_name ASC;

8️⃣ Display distinct department names:

    SELECT DISTINCT(department) FROM employees;

9️⃣ Display first_name as Name and salary as Income:

    SELECT first_name as Name, salary as Income FROM employees;

🔟 Display employees whose name starts with ‘A’:
    
    SELECT * FROM employees WHERE first_name LIKE 'A%' 



DAY 2 :

1️⃣ Employees with salary greater than or equal to 65,000:

   SELECT * FROM employees WHERE salary>=65000;


2️⃣ Employees who are not in HR department:

    SELECT * FROM employees WHERE department != 'HR';

3️⃣ Employees working in HR or Marketing:

    SELECT * FROM employees WHERE department ='HR' OR department='Marketing';

4️⃣ Employees hired between 2018 and 2020:

    SELECT * FROM employees WHERE hire_date  BETWEEN '2018-01-01' AND '2020-01-01';

5️⃣ Employees whose first name starts with ‘E’:

    SELECT * FROM employees WHERE first_name LIKE 'E%';

6️⃣ Employees whose name ends with ‘a’:

    SELECT * FROM employees WHERE first_name LIKE '%a';

7️⃣ Employees with salary between 60,000 and 80,000:

    SELECT * FROM employees WHERE salary BETWEEN 60000 AND 80000;

8️⃣ Employees from IT department earning more than 70,000:

    SELECT * FROM employees WHERE department='IT' and salary > 70000 ;

9️⃣ Employees whose job title is not Manager:

    SELECT * FROM employees WHERE job_id != 'Manager' ;

🔟 Employees not working in London or Toronto:  


    SELECT * FROM employees WHERE Location != 'London' and Location != 'Toronto';


DAY 3:

1️⃣ Show all employees ordered by salary (highest first):

    SELECT * FROM employees ORDER BY salary DESC;

2️⃣ Show all employees ordered by hire date (oldest first):

    SELECT * FROM employees ORDER BY hire_date ASC;

3️⃣ Display unique departments:

    SELECT DISTINCT(department) FROM employees;

4️⃣ Display unique locations:

    SELECT DISTINCT(Location) FROM employees;

5️⃣ Show top 5 highest paid employees:

    SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

6️⃣ Show 3 lowest paid employees:

    SELECT * FROM employees ORDER BY salary ASC LIMIT 3;

7️⃣ Skip first 2 highest salaries and show next 3 employees:

    SELECT * FROM employees ORDER BY salary DESC LIMIT 3 OFFSET 2;

8️⃣ List employees ordered by department (A–Z) and salary (high–low):

    SELECT * FROM employees ORDER BY department ASC , salary DESC;

9️⃣ Show distinct job roles:

    SELECT DISTINCT(job_id) FROM employees;

🔟 Show latest 4 hired employees:

    SELECT * FROM employees ORDER BY hire_date DESC LIMIT 4;     


DAY 4 :

1️⃣ Find total number of employees:

    SELECT COUNT(first_name) AS total_employees FROM employees;

2️⃣ Find total salary paid to all employees:

    SELECT SUM(salary) AS total_salary FROM employees;

3️⃣ Find average salary of all employees:

    SELECT AVG(salary) AS average_salary FROM employees;

4️⃣ Find minimum salary:

    SELECT MIN(salary) AS minimum_salary FROM employees;

5️⃣ Find maximum salary:

    SELECT MAX(salary) AS maximum_salary FROM employees;

6️⃣ Find number of employees working in HR department:

    SELECT COUNT(first_name) AS hr_emp FROM employees WHERE department = 'HR';

7️⃣ Find average salary of IT department employees:

    SELECT AVG(salary) AS IT_AVG FROM employees WHERE department = 'IT';

8️⃣ Find total salary paid to employees in London:

    SELECT SUM(salary) AS total_london FROM employees WHERE location = 'London';

9️⃣ Find earliest hire date:

    SELECT MIN(hire_date) AS EARLIEST_HIRE FROM employees;

🔟 Find latest hire date:
   
    SELECT MAX(hire_date) AS LATEST_HIRE FROM employees;


DAY 5:

1️⃣ Find the number of employees in each department:

    SELECT department,COUNT(first_name) FROM employees GROUP BY department;

2️⃣ Find the total salary paid in each department:

    SELECT department,SUM(salary) FROM employees GROUP BY department;

3️⃣ Find the average salary of each department:

    SELECT department,AVG(salary) FROM employees GROUP BY department;

4️⃣ Find the departments having more than 2 employees:

    SELECT department,COUNT(first_name) AS emp FROM employees GROUP BY department HAVING emp>2;

5️⃣ Find the departments where the average salary is greater than 70,000:

    SELECT department,AVG(salary) AS salary_dep FROM employees GROUP BY department HAVING salary_dep>70000;

6️⃣ Find the total salary paid by each location:

    SELECT location,SUM(salary) FROM employees GROUP BY location;

7️⃣ Find the locations having more than 3 employees:

    SELECT location,COUNT(first_name) AS L_emp FROM employees GROUP BY location HAVING L_emp>3;

8️⃣ Find the departments where the minimum salary is greater than 50,000:

    SELECT department,MIN(salary) AS mini_sal FROM employees GROUP BY department HAVING mini_sal>50000;

9️⃣ Find the departments where the maximum salary is less than 100,000:

    SELECT department,MAX(salary) AS MAX_SAL FROM employees GROUP BY department HAVING MAX_SAL<100000;

🔟 Find the departments with total salary greater than 200,000:

    SELECT department,SUM(salary) AS total_sal FROM employees GROUP BY department HAVING total_sal>200000;

'''