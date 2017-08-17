import sqlite3

db = 'nameofdatabase.db'
con = sqlite3.connect(db)

c = con.cursor() ##using a connection to the database, create a cursor object (looking for things in dbase -- like crawler)

#c.execute() takes in a string

#you can type as much as you want using the three apestropes'''

c.execute('''
			CREATE TABLE name(ID Integer Primary Key Autoincrement, fname Text, lname Text)
		''')
c.execute('''
			INSERT INTO name(fname, lname) VALUES ("John", "Wayne")

			SELECT * FROM name
		''')
con.commit()

# count_function:
# 	select count(*) from employeee_salary where country = 'china'




