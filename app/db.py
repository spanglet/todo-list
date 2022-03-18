
from .sql_util import connect_sql

host = "mysqldb"
db = "flax"

def db_init(reinit=False):

  mydb = connect_sql(host, None)
  cursor = mydb.cursor(buffered=True)

  # Skip db creation if database already exists
  cursor.execute("SHOW DATABASES LIKE %s", [db])
  if cursor.rowcount and not reinit:
    return 'db already exists'

  
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
    listID INTEGER DEFAULT 1,
    primary Key (taskID),
    foreign Key (categoryID) REFERENCES categories(categoryID),
    foreign Key (listID) REFERENCES lists(id)
  '''

  categoryTable = '''
    name VARCHAR(255), 
    categoryID INTEGER NOT NULL,
    description VARCHAR(255),
    primary Key (categoryID)
  '''

  listTable = '''
    name VARCHAR(255), 
    id INTEGER NOT NULL AUTO_INCREMENT,
    description VARCHAR(255),
    primary Key (id)
  '''

  # Table to hold user authentication data
  userTable = '''
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
  '''
  mydb = connect_sql(host, db)
  cursor = mydb.cursor()

  cursor.execute("CREATE TABLE users ({})".format(userTable))
  cursor.execute("CREATE TABLE lists ({})".format(listTable))
  cursor.execute("CREATE TABLE categories ({})".format(categoryTable))
  cursor.execute("CREATE TABLE tasks ({})".format(taskTable))
  cursor.close()

  return 'init database'


