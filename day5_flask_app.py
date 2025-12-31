from flask import Flask, jsonify
import psycopg

app = Flask(__name__)

def get_connection():
    return psycopg.connect(
        dbname="python_job_prep",
        user="postgres",
        password="limbu",
        host="localhost",
        port="5432"
    )

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    result = []
    for user in users:
        result.append({
            "id":user[0],
            "name":user[1],
            "age":user[2],
            "email":user[3]
        })
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)