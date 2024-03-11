from enum import Enum
from console import Console
import traceback

# Class responsible for mapping user input to the correct method.
class Controller:
  
  class Menu(Enum):
    MAIN = None,
    MEMBER = None,
    BOOKS = None,
    SUBJECTS = None,
  
  menu = Menu.MAIN
  action = Console.Action
  input = None
  quit = False
  subjects = None
  
  
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
      case self.Menu.BOOKS:
        self.action = self.console.books_menu("BOOKS MENU", [""]) 
      case self.Menu.SUBJECTS:
        self.input = self.console.subjects_menu("SUBJECTS MENU", self.subjects)
        self.action = Console.Action.BOOKS
        
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
      case Console.Action.BOOKS:
        self.__display_book_details()
      case _:
        return None
        
  def __register_member(self):
    data = self.console.get_member_data()
    self.bookstore.create_member(data)
    self.console.action_succeded("Member Registration")

  def __login_member(self):
    credentials = self.console.get_member_credentials()
    try:
      self.bookstore.authenticate_member(credentials)
    except PermissionError:
      pass

  def __browse_by_subject(self):
    self.subjects = self.bookstore.get_subjects()
  
  def __display_book_details(self):
    self.books = self.bookstore.get_books_by_subject(self.subjects[self.input - 1])
    
  def __quit_app(self):
    self.quit = True