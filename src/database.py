from mysql.connector import connect
import traceback

class Database:
  
  # establish connection to the mysql database
  def __init__(self, host, user, password, database):
    try:
      self.connection = connect(host=host, user=user, password=password, database=database)
    except:
      traceback.print_exc()