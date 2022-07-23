import sqlite3
con=sqlite3.connect('database3.sqlite3')
cur=con.cursor()
cur.execute('''SELECT firstname,lastname,salary
 FROM employee3 ORDER BY salary DESC  ''')
emp=cur.fetchall()
n=int(input('Enter value of n:'))
print(emp[n-1])