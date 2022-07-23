import sqlite3 as sql
con=sql.connect('database3.sqlite3')
rb=con.execute('''select firstname,lastname,salary from employee3 where salary>(select avg(salary) from employee3)''')
for i in rb:
	print(i)
	