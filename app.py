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
