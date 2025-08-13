import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)

mycursor = mydb.cursor()

mycursor.execute(
    "create table if not exists employee(id int auto_increment primary key,name varchar(20),age int,salary int)")

# also we insert datata by above function which is mycursor.execute but also we create a function for multiple insertion operation


def insert(name, age, salary):  # id is on auto increment so no need to insert id
    mycursor.execute("insert into employee(name,age,salary) values(%s,%s,%s)",
                     (name, age, salary))
    mydb.commit()


insert("saqib", 22, 20000)
