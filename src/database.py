from mysql.connector import connect
import traceback

class Database:
  
  # establish connection to the mysql database
  def __init__(self, host, user, password, database):
    try:
      self.connection = connect(host=host, user=user, password=password, database=database)
    except:
      traceback.print_exc()
      
  def insert (self, table, data):
    try:
      # Create a dictionary of attribute names and values
      attributes = {attr: getattr(data, attr) for attr in dir(data) if not attr.startswith('__') and not callable(getattr(data, attr))}
      # Format the values for SQL query
      values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in attributes.values()])
      # Construct the query
      query = f"INSERT INTO {table} ({', '.join(attributes.keys())}) VALUES ({values})"
      self.__execute_with_commit(query)
    except Exception as e:
      print(e)
   
  def select_all (self, query):
    return self.__execute_with_fetchall(query)
  
  def select_one (self, query):
    return self.__execute_with_fetchone(query)
    
     
  #get cursor
  def __get_cursor__(self):
    return self.connection.cursor()
    
  #execute and fetch all reaults
  def __execute_with_fetchall(self,query):
    with self.__get_cursor__() as cursor:
      cursor.execute(query)
      return cursor.fetchall()
    
    #execute and fetch all reaults
  def __execute_with_fetchone(self,query):
    with self.__get_cursor__() as cursor:
      cursor.execute(query)
      result = cursor.fetchone()  # Fetch one row
      for _ in cursor:  # Consume or discard remaining rows
        pass
    return result
       
  #execute with commit
  def __execute_with_commit(self,query):
    with self.__get_cursor__() as cursor:
      cursor.execute(query)
      self.connection.commit()