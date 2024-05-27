import sqlite3

##connect to sqlite
connection = sqlite3.connect("student.db")


## create a cursor object to indert record, create table, retrieve
cursor = connection.cursor()

table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);

"""
cursor.execute(table_info)


## insert into the table 
cursor.execute('''INSERT INTO STUDENT values('adam','data science','A',90)''')
cursor.execute('''INSERT INTO STUDENT values('nick','data science','A',80)''')
cursor.execute('''INSERT INTO STUDENT values('deepak','data analyst','B',95)''')
cursor.execute('''INSERT INTO STUDENT values('deepak','data science','A',75)''')
cursor.execute('''INSERT INTO STUDENT values('vikash','computer science','C',60)''')
cursor.execute('''INSERT INTO STUDENT values('lopez','DEVOPS','D',90)''')
cursor.execute('''INSERT INTO STUDENT values('zia',' ','A',60)''')

## DIsplay all the records

print(" the records are...")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## CLOSE THE connection
connection.commit()
connection.close()