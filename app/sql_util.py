
import mysql.connector

# Connect to SQL database via MySQL-Python connector
def connect_sql(sql_host,sql_db):
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="abc123",
        database=sql_db
    )

def insertRow (db,tableName, vals):

    cursor = db.cursor()

    query = ("INSERT INTO " + tableName + "(name,description) "
            "VALUES (%s, %s)")
    vals = tuple(vals)

    cursor.execute(query, vals)
    db.commit()

    row_id = cursor.lastrowid
    cursor.close()

    return row_id

# Update row in given table, requires primary key
def updateRow (db,tableName, json):

    cursor = db.cursor()

    query = ("UPDATE " + tableName +
            createUpdateStatement(json) +
            "WHERE taskID = %s")

    cursor.execute(query, tuple(json.values()))
    db.commit()
    cursor.close()

def removeRow (db, tableName, task_id):

    cursor = db.cursor()
    query = ("DELETE FROM " + tableName +
            " WHERE taskID = %s")

    cursor.execute(query, [task_id])

    db.commit()
    cursor.close()

def createUpdateStatement (json):
    ''' Create string for update query from json 
    '''

    statement = "= %s, ".join([key for key in json.keys()])
    return statement + " = %s"

