from database import Database
from dotenv import dotenv_values

# Class responsible for the main business logic.
class BookStore:
  
  # Load env variables
  config = dotenv_values(".env")
  
  def __init__(self):
    self.database = Database(self.config["DB_HOST"], self.config["DB_USERNAME"], self.config["DB_PASSWORD"], self.config["DB_NAME"])
  
  def create_member(self, data):
    self.database.insert("MEMBER", data)