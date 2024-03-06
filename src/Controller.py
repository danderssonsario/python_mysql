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
      
  def display_menu(self):
    match self.menu:
      case self.Menu.MAIN:
        self.action = self.console.main_menu("MAIN MENU", ["Member Login", "Member Registration", "Quit"])
  
        
  def do_action(self):
    match self.action:
      case Console.Action.QUIT:
        self.quit = True