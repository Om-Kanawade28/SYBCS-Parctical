import psycopg2
conn = None
try:
    print("Connecting")
    conn = psycopg2.connect(database = "mydata",
                            user = "postgres",
                            host = "localhost",
                            password = "omsai@2024#",
                            port = 5432)
    cur = conn.cursor()
    #cur.execute("""create table student(id int primary key,name char(50) not null,address varchar(50) not null,dob date not null);""")
    cur.execute("""insert into student values(1,'om','pune','2005-09-20')""")
    conn.commit()
    cur.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print("closed")