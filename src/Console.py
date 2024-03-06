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
  
  def get_member_data():
    print()
    print("New Member Registration")
    
    fname = input("First name: ")
    lname = input("Last name: ")
    address = input("Street address: ")
    city = input("City: ")
    state = input("State: ")
    zip =input("Zip: ")
    phone = input("Phone: ")
    email = input("Email address: ")
    print()
    password = input("Enter a password: ")
    
    return MemberData(fname, lname, address, city, state, zip, phone, email, password)
  
class MemberData:
  def __init__(self, fname, lname, address, city, state, zip, phone, password):
    self.fname = fname
    self.lname = lname
    self.address = address
    self.city = city
    self.state = state
    self.zip = zip
    self.phone = phone
    self.password = password

  def action_succeded(self, message):
    print()
    print(message + "has been done successfully!")
    input("Enter any key to continue")