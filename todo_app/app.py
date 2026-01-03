from flask import Flask, render_template, request
import psycopg

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", task_list=get_task())

def get_connection():
    return psycopg.connect(
        dbname = "todo_app",
        user = "postgres",
        password = "limbu",
        host = "localhost",
        port = "5432"
    )

def get_task():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("Select * from tasks")
    task_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return task_list

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form["task_name"]
    if (task_name.strip()):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("Insert into tasks (task_name) values (%s)", (task_name,))
        conn.commit()
        conn.close()
        cursor.close()
    return render_template("index.html", task_list = get_task())

@app.route("/delete/<int:i>")
def delete_task(i):
    conn = get_connection()
    cursor = conn.cursor()
   
    cursor.execute("delete from tasks where id = %s", (i,))
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("index.html", task_list=get_task())

app.run(debug=True)