from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to a SQLite database
conn = sqlite3.connect("form_data.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table to store form data
cursor.execute("""CREATE TABLE IF NOT EXISTS form_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    message TEXT
                )""")
conn.commit()


# Route handler to show the form
@app.route("/")
def show_form():
    return render_template("form.html")


# Route handler for submitting the form
@app.route("/submit", methods=["POST"])
def submit_form():
    # Get the form data
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Save the form data to the database
    cursor.execute("""INSERT INTO form_data (name, email, message)
                      VALUES (?, ?, ?)""", (name, email, message))
    conn.commit()

    # Redirect to the list of items
    return redirect(url_for("list_items"))

# Route handler to display all items
@app.route("/items")
def list_items():
    cursor.execute("SELECT * FROM form_data")
    items = cursor.fetchall()
    return render_template("items.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)