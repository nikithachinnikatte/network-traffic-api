from flask import Flask, jsonify
import sqlite3
from analyzer import process_pcap

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        src TEXT,
        dst TEXT,
        protocol TEXT
    )
    """)

    conn.commit()
    conn.close()

# Insert data into DB
def insert_data(df):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO traffic (src, dst, protocol) VALUES (?, ?, ?)",
            (row['src'], row['dst'], row['protocol'])
        )

    conn.commit()
    conn.close()

# Home route
@app.route("/")
def home():
    return "API is running"

# Load PCAP data
@app.route("/load")
def load_data():
    df = process_pcap("test.pcapng")
    insert_data(df)
    return "Data Loaded Successfully"

# Top IPs
@app.route("/top-ips")
def top_ips():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT src, COUNT(*) as count
        FROM traffic
        GROUP BY src
        ORDER BY count DESC
        LIMIT 5
    """)

    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

# Protocol distribution
@app.route("/protocols")
def protocols():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT protocol, COUNT(*) as count
        FROM traffic
        GROUP BY protocol
    """)

    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

# Run server
if __name__ == "__main__":
    init_db()
    app.run(debug=True)