
import mysql.connector


# Connect to SQL database via MySQL-Python connector
def connect_sql(sql_host,sql_db):
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="abc123",
        database=sql_db
    )

def insertRow (db,tableName, rowValues):

    cursor = db.cursor()

    query = ("INSERT INTO " + tableName + "(name,description) "
            "VALUES (%s, %s)")
    vals = ("TESTING", "TEST")

    cursor.execute(query, vals)
    db.commit()
    cursor.close()

