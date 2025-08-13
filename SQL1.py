import sqlite3

conn = sqlite3.connect("examole.db")
cursor = conn.cursor()

cursor.execute('''Create table if not exists users(id int primary key autoincreament , name text NOTNULL , age int NOT NULL)''')

print("table created or already exists...")

def insert_user(name , age):
    cursor.execute("insert into users(name , age) values(?,?) ,(name , age )")

    print(f"user {name} added")

insert_user("saqib", 22)
insert_user("bob", 25)

def update_user_age(name , new_age):
    cursor.execute("update user set age=? wghere name = ?",(new_age,name))
    conn.commit()
    print(f"user {name} age updated to {new_age}")

update_user_age("bob", 30)

def delete_user(name):
    cursor.execute("DELETE FROM user WHERE name  = ? ",(name))
    conn.commit()
    print(f"user {name} deleted")

delete_user("bob")

def show_user():
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    print("current users:")
    for row in rows:
        print(row)

show_user()
conn.close()
    
