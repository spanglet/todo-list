
import mysql.connector
from .sql_util import connect_sql

host = "mysqldb"
db = "flax"

def db_init():
  mydb = connect_sql(host, None)
  cursor = mydb.cursor()

  print("Creating Database")
  cursor.execute("DROP DATABASE IF EXISTS flax")
  cursor.execute("CREATE DATABASE flax")
  cursor.close()

  taskTable = '''
    name VARCHAR(255), 
    taskID INTEGER NOT NULL AUTO_INCREMENT,
    description VARCHAR(255),
    categoryID INTEGER,
    priority INTEGER,
    trueDueDate DATETIME,
    preferredDueDate DATETIME,
    dependantsID INTEGER REFERENCES Tasks(taskID),
    startDate DATETIME,
    primary Key (taskID),
    foreign Key (categoryID) REFERENCES categories(categoryID)
  '''

  categoryTable = '''
    name VARCHAR(255), 
    categoryID INTEGER NOT NULL,
    description VARCHAR(255),
    primary Key (categoryID)
  '''

  # Table to hold user authentication data
  userTable = '''
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
  '''
  mydb = connect_sql(host, db)
  cursor = mydb.cursor()

  # Drop Tables if previously created
  cursor.execute("DROP TABLE IF EXISTS tasks")
  cursor.execute("DROP TABLE IF EXISTS categories")
  cursor.execute("DROP TABLE IF EXISTS users")

  cursor.execute("CREATE TABLE categories ({})".format(categoryTable))
  cursor.execute("CREATE TABLE tasks ({})".format(taskTable))
  cursor.execute("CREATE TABLE users ({})".format(userTable))
  cursor.close()

  return 'init database'


