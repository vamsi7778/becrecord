import sqlite3 as sql
con=sql.connect('database3.sqlite3')
rd=con.execute('''select avg(salary),count(employee_id)department_id from employee3 group by department_id having count(employee_id)>10''')
for i in rd:
	print(i)