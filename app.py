from flask import Flask, render_template

import sqlite3

#setting up the db
conn = sqlite3.connect('interns.db')
cursor = conn.cursor()

#create user table
def create_user_table():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    password TEXT)
                      ''')
    conn.commit()
    conn.close()

#call the function to create the table
create_user_table()

#select users
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


app = Flask(__name__)

#routing
@app.route("/")
def home():
    #processing..
    interns = ['Joshua', 'John', 'Jane', 'Mary']
    return render_template("home.html", item=interns)

@app.route("/about")
def about():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)












