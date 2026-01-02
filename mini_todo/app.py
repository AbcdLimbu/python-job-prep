from flask import Flask, render_template, request

app = Flask(__name__)

todoList = []

@app.route("/")
def home():
    return render_template("index.html", taskList=todoList)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["taskName"]
    if task.strip():
        todoList.append(task)
    return render_template("index.html", taskList=todoList)

@app.route("/delete/<int:i>")
def delete_task(i):
    if (0 <= i < len(todoList)):
        todoList.pop(i)
    return render_template("index.html", taskList=todoList)

app.run(debug=True)