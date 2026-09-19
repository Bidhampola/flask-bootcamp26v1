from flask import Flask, render_template,request, redirect, url_for

import sqlite3

#setting up the db


#create user table
def create_user_table():
    conn = sqlite3.connect('interns.db')
    cursor = conn.cursor()
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
    conn = sqlite3.connect('interns.db')
    cursor = conn.cursor()
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

#user creation
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        #inserting into the db
        conn = sqlite3.connect('interns.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email,password) VALUES (?,?)", (email,password))
        conn.commit()
        conn.close()

        return redirect(url_for("register"))
        

    else:
        return render_template("register.html")

#viewing users
@app.route("/users")
def view_users():
    conn = sqlite3.connect('interns.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)












