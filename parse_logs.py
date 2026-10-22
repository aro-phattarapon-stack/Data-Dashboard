from pprint import pprint
import sqlite3

clean_log = []

with open("access.log", "r", encoding="utf-8") as logs:
    for log in logs:
        Seperate_log = log.split()

        tup = (
            Seperate_log[0],
            Seperate_log[3].strip("[]"),
            Seperate_log[4].strip("\""),
            Seperate_log[5],
            int(Seperate_log[7]),
            int(Seperate_log[8])
        )

        clean_log.append(tup)
pprint(clean_log[:10])

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

conn.execute("""
    CREATE TABLE IF NOT EXISTS access_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        timestamp TEXT,
        method TEXT,
        endpoint TEXT,
        status INTEGER,
        size INTEGER
    )
""")

cursor.executemany("""
    INSERT OR REPLACE INTO access_logs (ip, timestamp, method, endpoint, status, size)
    VALUES (?, ?, ?, ?, ?, ?)
""", clean_log)

conn.commit()
conn.close()
print(f"{len(clean_log)} บันทึกเรียบร้อย")