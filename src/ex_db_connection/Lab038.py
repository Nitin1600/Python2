# import psycopg2
#
# conn=psycopg2.connect(database="postgres", user="postgres", password="admin",
#                       host="127.0.0.1", port="5432")
#
# print("Opened database successfully")

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin", host="127.0.0.1", port="5432")
#
# print("Database connected sucessfully")
#
# cur = conn.cursor()
# cur.execute("""CREATE TABLE COMPANY27_12
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             ADDRESS CHAR(50),
#             SALARY REAL);""")
#
# print("Table created sucessfully")
# conn.commit()
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
#                         host="127.0.0.1", port="5432")
#
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY27_12_2
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             ADDRESS CHAR(50),
#             SALARY REAL);''')
# print("Database connected successfully")
# conn.commit()
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
#                         host="127.0.0.1", port="5432")
#
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("INSERT INTO company27_12_2 (ID,NAME,AGE,ADDRESS,SALARY)\
#         VALUES (1, 'Paul', 22, 'KA', 12000)");
# cur.execute("INSERT INTO COMPANY27_12_2(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES (2,'Tom', 24, 'TN', 14000)");
# cur.execute("INSERT INTO COMPANY27_12_2(ID,NAME,AGE,ADDRESS,SALARY)\
#     VALUES(3,'David',25,'Perth',50000)");
# cur.execute("INSERT INTO COMPANY27_12_2(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES (4, 'Stuart', 28, 'GA', 18000)");
#
# conn.commit()
# print("Inserted records successfully")
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
#                         host="127.0.0.1", port="5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("SELECT id,name,age,address,salary from COMPANY27_12_2")
# rows = cur.fetchall()
#
# for row in rows:
#     print("id = ", row[0])
#     print("name = ", row[1])
#     print("age = ", row[2])
#     print("address = ", row[3])
#     print("salary = ", row[4],"\n")
#
# print("Fetched records successfully")
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
#                         host="127.0.0.1", port="5432")
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("UPDATE COMPANY27_12_2 set SALARY=25000.0 where ID=1")
# conn.commit()
# print("Total number of rows updated: ", cur.rowcount)
#
# cur.execute("SELECT id,name,age,address,salary from COMPANY27_12_2")
# rows = cur.fetchall()
# for row in rows:
#     print("id = ", row[0])
#     print("name = ", row[1])
#     print("age = ", row[2])
#     print("address = ", row[3])
#     print("salary = ", row[4], "\n")
#
# print("Records updated and fetched successfully")
# conn.close()

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="admin",
                        host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute("DELETE from COMPANY27_12_2 where ID=2")
conn.commit()
print("Total number of rows deleted: ", cur.rowcount)

cur.execute("SELECT id,name,age,address,salary from COMPANY27_12_2")
rows = cur.fetchall()
for row in rows:
    print("id = ", row[0])
    print("name = ", row[1])
    print("age = ", row[2])
    print("address = ", row[3])
    print("salary = ", row[4], "\n")

print("Deleted a row and fetched the records successfully")
conn.close()