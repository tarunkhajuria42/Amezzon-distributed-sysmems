import mysql.connector as conn

db = conn.connect("localhost", "testuser", "test123", "TESTDB")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version: %s" % data)
db.close()