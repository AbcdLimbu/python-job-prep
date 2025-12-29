import psycopg

conn = psycopg.connect(
    dbname="python_job_prep",
    user="postgres",
    password="limbu",
    host="localhost",
    port="5432" 
)

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)",
    ("John Camo", 25, "john@example.com")
)

conn.commit()

cursor.execute("Select * from users")
rows = cursor.fetchall()

for row in rows:
    print(row)


cursor.close()
conn.close()