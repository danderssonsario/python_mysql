from database import Database
from dotenv import dotenv_values

# Class responsible for the main business logic.
class BookStore:
  
  # Load env variables
  config = dotenv_values(".env")
  
  def __init__(self):
    self.database = Database(self.config["DB_HOST"], self.config["DB_USERNAME"], self.config["DB_PASSWORD"], self.config["DB_NAME"])
  
  def create_member(self, data):
    self.database.insert("members", data)
    
  def get_subjects(self):
    return self.database.select_all("SELECT DISTINCT subject FROM books ORDER BY subject;")
  
  def authenticate_member(self, credentials):
    user = self.database.select_one(f"""SELECT userid from  members WHERE email = {credentials.email} AND password = {credentials.password}""")
    if (user):
      return user
    else:
      raise PermissionError()
    
  def get_books_by_subject(self, subject):
    return self.database.select_all(f"""SELECT * FROM books WHERE subject = {subject};""")
  
  def get_books_by_author(self, search):
    return self.database.select_all(f"""SELECT * FROM books WHERE author LIKE '%{search}%'""")
  
  def get_books_by_title(self, search):
    return self.database.select_all(f"""SELECT * FROM books WHERE title LIKE '%{search}%'""")
  
  def add_to_cart(self, data):
    self.database.insert("cart", data)