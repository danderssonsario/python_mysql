from enum import Enum

# Class responsible for serving menu and prompting user for input.
class Console:
  class Action(Enum):
    QUIT = 1,
    MEMBER_LOGIN = 1,
    MEMBER_REGISTER = 1,
  
  def main_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    self.__prompt_for_action(len(options))


  def __print_header(self, title):
    print()
    print("***********************************************************")
    print("***                                                     ***")
    print("***                 " + title + "                       ***")
    print("***                                                     ***")   
    print("***********************************************************") 

  def __print_options(self, options):
    print()
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}") 

  def __prompt_for_action(self, maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Enter choice:")
        try:
            if int(choice) in [x for x in range(1,maxOptions+1)]:
                selectedOption = int(choice)
            else:
                print("Invalid input: please select the available options.")    
        except Exception:
            selectedOption = None
            print("Invalid input: it should be a number")           
    return  selectedOption