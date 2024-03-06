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
      # TODO: FIX THE QUERY
       insert_query = f""" INSERT INTO {table} ({', '.join(data.keys())}) VALUES("{data.fname}","{data.lname}","{data.address}","{data.city}","{data.state}","{data.zip}","{data.phone}","{data.email}","{data.password}","{data.fname}","{data.lname}","{data.address}","{data.city}","{data.state}","{data.zip}","{data.phone}","{data.email}","{data.password}");   """
       self.__execute_with_commit(insert_query)
       print("Adding new  employee was succsessful!")
    except Exception as e:
        print("ADDING employee operation is FAILD!")
        print(e)
        
  #get cursor
  def __get_cursor__(self):
    return self.connection.cursor()
    
  #execute and fetch all reaults
  def __execute_with_fetchall(self,query):
    with self.__get_cursor__() as cursor:
      cursor.execute(query)
      return cursor.fetchall()
       
  #execute with commit
  def __execute_with_commit(self,query):
    with self.__get_cursor__() as cursor:
      cursor.execute(query)
      self.connection.commit()