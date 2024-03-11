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
    SEARCH = None
  
  menu = Menu.MAIN
  action = Console.Action
  input = None
  quit = False
  subjects = None
  books = None
  book_index = 0
  no_of_books = 0
  user = None
  
  
  def __init__(self, console, bookstore):
    self.console = console
    self.bookstore = bookstore
    
  def run (self):
    try:
      while not self.quit:
        self.display_menu()
        self.do_action()
    except:
      traceback.print_exc()
      
  def display_menu(self):
    match self.menu:
      case self.Menu.MAIN:
        self.action = self.console.main_menu("MAIN MENU", ["Member Login", "Member Registration", "Quit"])
      case self.Menu.MEMBER:
        self.action = self.console.member_menu("MEMBER MENU", ["Browse by Subject", "Search by Author/Title", "Checkout", "Logout"])
      case self.Menu.BOOK_MENU:
        self.input = self.console.books_menu("BOOKS MENU", len(self.books), self.books[self.book_index: self.book_index + self.no_of_books])        
        match self.input:
          case "":
            self.action = Console.Action.BACK
          case "n":
            self.action = Console.Action.BROWSE_NEXT
          case _:
            self.action = Console.Action.ADD_TO_CART
        
      case self.Menu.SUBJECTS:
        self.input = self.console.subjects_menu("SUBJECTS MENU", self.subjects)
        self.action = Console.Action.BOOKS
      case self.Menu.SEARCH:
        self.action = self.console.search_menu("SEARCH MENU", ["Author Search", "Title Search", "Go Back To Main Menu"])
      case _:
        pass
        
  def do_action(self):
    match self.action:
      # Main Menu Actions
      case Console.Action.MEMBER_LOGIN:
        self.__login_member()
        self.menu = self.Menu.MEMBER
      case Console.Action.MEMBER_REGISTER:
        self.__register_member()
      case Console.Action.QUIT:
        self.__quit_app()
        self.quit = True
      # Member Menu Actions
      case Console.Action.BROWSE:
        self.__browse_by_subject()
        self.menu = self.Menu.SUBJECTS
      case Console.Action.SEARCH: 
        self.menu = self.Menu.SEARCH 
      # Browse by Subject actions
      case Console.Action.BOOKS:
        self.__display_book_details()
        self.no_of_books = 2
        self.menu = self.Menu.BOOK_MENU
      case Console.Action.BACK_SUBJECT:
        self.menu = self.Menu.SUBJECTS
      case Console.Action.BROWSE_NEXT:
        self.bookIndex = self.bookIndex + 1
      case Console.Action.ADD_TO_CART:
        self.__add_to_cart()
      case Console.Action.SEARCH_BY_AUTHOR:
        self.__search_by_author()
        self.no_of_books = 3
        self.menu = self.Menu.BOOK_MENU
      case Console.Action.SEARCH_BY_TITLE:
        self.__search_by_title()
        self.no_of_books = 3
        self.menu = self.Menu.BOOK_MENU
      case Console.Action.BACK_MAIN:
        self.menu = self.Menu.MEMBER
      case _:
        return None
        
  def __register_member(self):
    data = self.console.get_member_data()
    self.bookstore.create_member(data)
    self.console.action_succeded("Member Registration")

  def __login_member(self):
    credentials = self.console.get_member_credentials()
    try:
      self.user = self.bookstore.authenticate_member(credentials)
    except PermissionError:
      pass

  def __browse_by_subject(self):
    self.subjects = self.bookstore.get_subjects()
  
  def __display_book_details(self):
    self.books = self.bookstore.get_books_by_subject(self.subjects[self.input - 1])
  
  def __add_to_cart(self):
    qty = self.console.prompt_for_quantity()
    self.bookstore.__add_to_cart(CartData(qty, self.input, self.user.userid))
  
  def __search_by_author(self):
    search_string = self.console.get_search_string()
    self.books = self.bookstore.get_books_by_author(search_string)
  
  def __search_by_title(self):
    search_string = self.console.get_search_string()
    self.books = self.bookstore.get_books_by_title(search_string)
    
    
  def __quit_app(self):
    self.quit = True
    
class CartData:
  def __init__(self, qty, isbn, userid):
    self.qty = qty
    self.isbn = isbn
    self.userid = userid
 
