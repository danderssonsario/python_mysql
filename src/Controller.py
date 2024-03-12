from enum import Enum
from console import Console
import traceback

# Class responsible for mapping user input to the correct method.
class Controller:
  
  class Menu(Enum):
    MAIN = None,
    MEMBER = None,
    BOOK_MENU = None,
    SUBJECTS = None,
    SEARCH = None,
    CHECKOUT = None
    
  class Action(Enum):
    QUIT = None,
    MEMBER_LOGIN = None,
    MEMBER_REGISTER = None,
    BROWSE = None,
    SEARCH = None,
    CHECKOUT = None,
    LOGOUT = None,
    BOOKS = None,
    BROWSE_NEXT = None,
    ADD_TO_CART = None
    BACK_SUBJECT = None,
    BACK_MEMBER = None,
    SEARCH_BY_AUTHOR = None,
    SEARCH_BY_TITLE = None
    
  
  menu = "MAIN"
  action = None
  input = None
  quit = False
  subjects = None
  books = None
  book_index = 0
  no_of_books_to_display = 0
  user = None
  checkout_data = None
  order = None
  
  def __init__(self, console, bookstore):
    self.console = console
    self.bookstore = bookstore
    
  def run (self):
    try:
      while not self.quit:
        self.display_menu()
    except:
      traceback.print_exc()
      # self.run()
      
  def display_menu(self):
    if self.menu == "MAIN":
        self.input = self.console.main_menu("MAIN MENU", ["Member Login", "Member Registration", "Quit"])
        
        if self.input == "1":
            self.__login_member()
            self.menu = "MEMBER"
        elif self.input == "2":
            self.__register_member()
        elif self.input == "3":
            self.__quit_app()
        else:
            return None
      
    elif self.menu == "MEMBER":
        self.input = self.console.member_menu("MEMBER MENU", ["Browse by Subject", "Search by Author/Title", "Checkout", "Logout"])
          
        if self.input == "1":
            self.__browse_by_subject()
            self.menu = "SUBJECTS"
        elif self.input == "2":
            self.menu = "SEARCH"
        elif self.input == "3":
            self.__checkout()
        elif self.input == "4":
            self.user = None
            self.menu = "MAIN"
        else:
            return None       

    elif self.menu == "SUBJECTS":
        self.input = self.console.subjects_menu(self.subjects)
        self.books = self.bookstore.get_books_by_subject(self.subjects[int(self.input) - 1])
        self.no_of_books_to_display = 2
        self.menu = "BOOK_MENU"
        
    elif self.menu == "SEARCH":
        self.input = self.console.search_menu("SEARCH MENU", ["Author Search", "Title Search", "Go Back To Main Menu"])
        
        if self.input == "1":
            self.__search_by_author()
            self.no_of_books_to_display = 3
            self.menu = "BOOK_MENU"
        elif self.input == "2":
            self.__search_by_title()
            self.no_of_books_to_display = 3
            self.menu = "BOOK_MENU" 
        elif self.input == "3":
            self.menu = "MEMBER"
        else:
            return None
          
    elif self.menu == "BOOK_MENU":
        self.input = self.console.books_menu(len(self.books), self.books[self.book_index: self.book_index + self.no_of_books_to_display])
        
        if self.input == "":
            self.menu = "MEMBER"
            self.book_index = 0
        elif self.input == "n":
            self.book_index = self.book_index + self.no_of_books_to_display
        else:
            self.__add_to_cart()
            
    elif self.menu == "CHECKOUT":
        self.input = self.console.checkout_menu(self.checkout_data)
        
        if self.input.upper() == "Y":
          self.__proceed_checkout()
          self.menu = "ORDER"
        elif self.input.upper() == "N":
          self.menu = "MEMBER"
        else:
            return None
          
    elif self.menu == "ORDER":
      self.console.order_menu(self.order, self.checkout_data)
    else:
        pass

        
  def __register_member(self):
    data = self.console.get_member_data()
    self.bookstore.create_member(data)
    self.console.action_succeded("Member Registration")

  def __login_member(self):
    credentials = self.console.get_member_credentials()
    try:
      self.user = self.bookstore.authenticate_member(credentials)
    except PermissionError:
      print("Wrong credentials")

  def __browse_by_subject(self):
    self.subjects = self.bookstore.get_subjects()
  
  def __display_book_details(self):
    self.books = self.bookstore.get_books_by_subject(self.subjects[self.input - 1])
  
  def __add_to_cart(self):
    qty = self.console.get_quantity()
    self.bookstore.add_to_cart(CartData(qty, self.input, self.user))
  
  def __search_by_author(self):
    search_string = self.console.get_search_string()
    self.books = self.bookstore.get_books_by_author(search_string)
  
  def __search_by_title(self):
    search_string = self.console.get_search_string()
    self.books = self.bookstore.get_books_by_title(search_string)
    
  def __checkout(self):
    self.checkout_data = self.bookstore.get_checkout_data(self.user)
    self.menu = "CHECKOUT"
    
  def __proceed_checkout(self):
    self.bookstore.create_order(self.checkout_data, self.user)
    self.order = self.bookstore.get_order_data(self.user)
    self.menu = "ORDER"
      
  def __quit_app(self):
    self.quit = True
    
class CartData:
  def __init__(self, qty, isbn, userid):
    self.qty = qty
    self.isbn = isbn
    self.userid = userid
    
