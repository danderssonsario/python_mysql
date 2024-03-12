from database import Database
from dotenv import dotenv_values
from datetime import date

# Class responsible for the main business logic.
class BookStore:
  
  # Load env variables
  config = dotenv_values(".env")
  
  def __init__(self):
    self.database = Database(self.config["DB_HOST"], self.config["DB_USERNAME"], self.config["DB_PASSWORD"], self.config["DB_NAME"])
  
  def create_member(self, data):
    self.database.insert("members", data)
    
  def get_subjects(self):
    subjects = self.database.select_all("SELECT DISTINCT subject FROM books ORDER BY subject;")
    return [subject[0].strip("()',") for subject in subjects]
  
  def authenticate_member(self, credentials):
    user = self.database.select_one(f"""SELECT userid from members WHERE email = {credentials.email} AND password = {credentials.password}""")
    if (user):
      return user[0] # userid
    else:
      raise PermissionError()
    
  def get_books_by_subject(self, subject):
    return self.database.select_all(f"""SELECT * FROM books WHERE subject = '{subject}';""")
  
  def get_books_by_author(self, search):
    return self.database.select_all(f"""SELECT * FROM books WHERE author LIKE '%{search}%'""")
  
  def get_books_by_title(self, search):
    return self.database.select_all(f"""SELECT * FROM books WHERE title LIKE '%{search}%'""")
  
  def add_to_cart(self, data):
    self.database.insert("cart", data)
    
  def get_checkout_data(self, userid):
    items = self.database.select_all(f"""SELECT c.*, b.title, b.price FROM cart c JOIN books b ON c.isbn = b.isbn WHERE c.userid = '{userid}'""")
    total_price = 0
    
    for item in items:
      total_price = total_price + int(item[4]) * item[0]

    return Checkout(items, total_price)
  
  def create_order(self, userid):
    created = date.today()
    order_data = self.database.select_one(f"""SELECT address, city, zip from members WHERE userid = {userid}""")
    order = Order(created, order_data[0], order_data[1], order_data[2], userid)
    self.database.insert("order", order)

  def get_order_data(self, userid):
    return self.database.select_one(f"""SELECT o.*, m.fname, m.lname from orders JOIN members m ON o.userid = m.userid WHERE o.userid = {userid}""")
    
class Checkout:
  def __init__(self, items, total):
    self.items = items
    self.total = total
    
class CheckoutUser:
  def __init__(self, fname, lname, address):
    self.fname = fname
    self.lname = lname
    self.address = address
    
class Order:
  def __init__(self, created, shipAdress, shipCity, shipZip, userid, items):
    self.created = created
    self.shipAdress = shipAdress
    self.shipCity = shipCity
    self.shipZip = shipZip
    self.userid = userid
    self.items = items
