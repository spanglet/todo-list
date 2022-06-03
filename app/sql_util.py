from flask import jsonify
import mysql.connector




# Connect to SQL database via MySQL-Python connector
def connect_sql(sql_host,sql_db):
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="abc123",
        database=sql_db
    )

def insertRow (db,tableName, data):

    cursor = db.cursor()

    keyString = ",".join([key for key in data.keys()])
    valString = "(%s" + ",%s"*(len(data)-1) + ")"

    query = ("INSERT INTO " + tableName +
            "(" + keyString + ") " +
            "VALUES " + valString)

    vals = tuple(data.values())
    cursor.execute(query, vals)
    db.commit()

    row_id = cursor.lastrowid
    cursor.close()

    return row_id

def getAllRows(db,tableName):
    ''' Selects and returns all entries in given table
    '''

    cursor = db.cursor()
    cursor.execute("SELECT * FROM " + tableName)
 
    row_headers=[x[0] for x in cursor.description] 
 
    results = cursor.fetchall()
    json_data=[]
    for result in results:
      json_data.append(dict(zip(row_headers,result)))
 
    cursor.close()
 
    return jsonify(json_data)
    


# Update row in given table, requires primary key
def updateRow (db,tableName, json):

    cursor = db.cursor()

    query = ("UPDATE " + tableName +
            createUpdateStatement(json) +
            "WHERE taskID = %s")

    cursor.execute(query, tuple(json.values()))
    db.commit()
    cursor.close()

def removeRow (db, tableName, elem_id):

    cursor = db.cursor()
    query = ("DELETE FROM " + tableName +
            " WHERE id = %s")

    cursor.execute(query, [elem_id])

    db.commit()
    cursor.close()

def createUpdateStatement (json):
    ''' Create string for update query from json 
    '''

    statement = " = %s,".join([key for key in json.keys()])
    return statement + " = %s"

