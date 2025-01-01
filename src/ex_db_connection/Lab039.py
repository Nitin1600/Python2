import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
                        host="127.0.0.1", port="5432")

print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY28
            ("ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "ADDRESS CHAR(50),"
             "SALARY REAL");''')
print("Print table created successfully")

cur = conn.cursor()
cur.execute("INSERT INTO COMPANY28(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(1, 'Paul', 22, 'KA', 10000.0)")
cur.execute("INSERT INTO COMPANY28(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(2, 'Tom', 24, 'TN', 12000.0)")
cur.execute("INSERT INTO COMPANY28(ID,NAME,ADDRESS,SALARY)\
            VALUES(3, 'David', 26, 'KE', 14000.0)")
cur.execute("INSERT INTO COMAPNY28(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(4, 'Bethell', 28, 'TE', 18000.0)")

cur.execute("UPDATE COMPANY28 set SALARY=20000.0 where id=1")
conn.commit()
print("Total number of rows updated: ", cur.roecount)

cur = conn.cursor()
cur.execute("SELECT id,name,age,address,salary from COMPANY28")
rows = cur.fetchall()
for row in rows:
    print("id = ", row[0])
    print("name = ", row[1])
    print("age = ", row[2])
    print("address = ", row[3])
    print("salary = ", row[4], "\n")

print("Operation completed successfully")
conn.close()

cur = conn.cursor()
cur.execute("DELETE COMPANY28 where ID=2")
conn.commit()
print("Total number of rows updated: ", cur.rowcount)

cur.execute("SELECT id,name,age,address,salary from COMPANY28")
rows = cur.fetchall()
for row in rows:
    print("id = ", row[0])
    print("name = ", row[1])
    print("age = ", row[2])
    print("address = ", row[3])
    print("salary = ", row[4])

print("Operation done successfully")
conn.commit()
conn.close()
