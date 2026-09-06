from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASS",
    database="personal_website"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save_visitor", methods=["POST"])
def save_visitor():
    name = request.form["name"]

    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO visitors (name) VALUES (%s)",
        (name,)
    )

    db.commit()
    cursor.close()

    # Return to the website after saving
    return redirect("/")
@app.route("/visitor_count")
def visitor_count():
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM visitors")
    count = cursor.fetchone()[0]

    cursor.close()

    return str(count)


if __name__ == "__main__":
    app.run(debug=True)