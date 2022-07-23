import sqlite3 as sql
con=sql.connect('database3.sqlite3')
rb=con.execute('''select min(salary),max(salary),sum(salary),avg(salary) from employee3''')
for i in rb:
	print(i)