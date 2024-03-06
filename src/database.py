from mysql.connector import connect

class Database:
  
  # establish connection to the mysql database
  def __init__(self, username, password) -> None:
    self.connection = connect(host="localhost", user=username, password=password, database='book_store')