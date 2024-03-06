from enum import Enum
from Console import Console
import traceback

# Class responsible for mapping user input to the correct method.
class Controller:
  
  class Menu(Enum):
    MAIN = 1
  
  menu = Menu.MAIN
  action = Console.Action
  quit = False
  
  
  def __init__(self, console, bookStore):
    self.console = console
    self.bookStore = bookStore
    
  def run (self):
    try:
      while not self.quit:
        self.display_menu()
        self.do_action()
    except:
      traceback.print_exc()
      self.run()
      
  def display_menu(self):
    match self.menu:
      case self.Menu.MAIN:
        self.action = self.console.main_menu("MAIN MENU", ["Member Login", "Member Registration", "Quit"])
  
        
  def do_action(self):
    match self.action:
      case Console.Action.MEMBER_REGISTER:
        self.__register_member()
      case Console.Action.QUIT:
        self.quit = True
        
  def __register_member(self):
    memberData = self.console.get_member_data()
    # self.BookStore.create_member(memberData)
    self.console.action_succeded("Member Registration")
