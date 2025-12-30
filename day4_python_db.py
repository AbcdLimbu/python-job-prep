import psycopg

def get_connection():
    return psycopg.connect(
        dbname="python_job_prep",
        user="postgres",
        password="limbu",
        host="localhost",
        port="5432"
    )

def insert_user(name, age, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", (name, age, email)  
    )

    conn.commit()
    cursor.close()
    conn.close()

def fetch_user():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users"
    )
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return users


insert_user("Connect", "32", "connect@gmail.com")
insert_user("Home", "23", "home@gmail.com")

all_users = fetch_user()

for user in all_users:
    print(user)