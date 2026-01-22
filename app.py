from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_db_connection():
    return psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/")
def health():
    return "Flask app is running!"

@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)

    cur.execute("INSERT INTO users (name) VALUES ('Labdhi') RETURNING id;")
    conn.commit()

    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
