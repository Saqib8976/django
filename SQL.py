import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="saqib",
    # alter user in database if get error
    # run in mysql workbench
    # ALTER USER 'root'@'localhost'
    # IDENTIFIED WITH mysql_native_password BY 'root';
    # FLUSH PRIVILEGES;
)


cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(100) NOT NULL , age INT NOT NULL)''')


def insert_user(name, age):
    cursor.execute("INSERT INTO users (name , age) VALUES(%s,%s)", (name, age))
    conn.commit()


def update_user_age(name, new_age):
    cursor.execute(
        "UPDATE users SET age = %s WHERE name = %s",
        (new_age, name)
    )
    conn.commit()


def delete_user(name):
    cursor.execute("DELETE FROM users WHERE name = %s", (name,))
    conn.commit()


def show_users():
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)


insert_user("saqib", 30)
insert_user("bob", 25)
update_user_age("saqib", 22)
delete_user("bob")
show_users()

conn.close()
