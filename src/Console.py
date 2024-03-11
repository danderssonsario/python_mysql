from enum import Enum

# Class responsible for serving menu and prompting user for input.
class Console:
  class Action(Enum):
    QUIT = None,
    MEMBER_LOGIN = None,
    MEMBER_REGISTER = None,
    BROWSE = None,
    SEARCH = None,
    CHECKOUT = None,
    LOGOUT = None,
    BOOKS = None,
    BACK = None,
    BROWSE_NEXT = None,
    ADD_TO_CART = None
    
  
  def main_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    input = self.__prompt_for_input(len(options))

    match input:
      case "1":
        return self.Action.MEMBER_LOGIN
      case "2":
        return self.Action.MEMBER_REGISTER
      case "3":
        return self.Action.QUIT
      case _:
        return None

  def member_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    input = self.__prompt_for_input(len(options))

    match input:
      case "1":
        return self.Action.BROWSE
      case "2":
        return self.Action.SEARCH
      case "3":
        return self.Action.CHECKOUT
      case "4":
        return self.Action.LOGOUT
      case _:
        return None

  def subjects_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    return self.__prompt_for_input(len(options))

  def books_menu(self, title, books):
    self.__print_header(title)
    print(f"""{len(books)} books available on this subject""")
    for book in books:
      print (f"""Author: {book.author}""")
      print (f"""Title: {book.title}""")
      print (f"""ISBN: {book.isbn}""")
      print (f"""Price: {book.price}""")
      print (f"""Subject: {book.subject}""")


    print("Enter ISBN too add to Cart ")
    print("Press n + ENTER to continue browsing")
    print("Press ENTER to go back to menu")
    
    return input()

  def __print_header(self, title):
    print()
    print("***********************************************************")
    print("***               Online Book Store                     ***")
    print("***                 " + title + "                       ***")
    print("***                                                     ***")   
    print("***********************************************************") 

  def __print_options(self, options):
    print()
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}") 

  def __prompt_for_input(self, maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Enter choice:")
            
        try:
            if int(choice) in [x for x in range(1,maxOptions+1)]:
                selectedOption = choice
            else:
                print("Invalid input: please select the available options.")    
        except Exception:
            selectedOption = None
            print("Invalid input: it should be a number")           
    return  selectedOption
  
  def get_member_data(self):
    print()
    print("New Member Registration")
    
    fname = input("First name: ")
    lname = input("Last name: ")
    address = input("Street address: ")
    city = input("City: ")
    state = input("State: ")
    zip = input("Zip: ")
    phone = input("Phone: ")
    email = input("Email address: ")
    print()
    password = input("Enter a password: ")
    
    return MemberData(fname, lname, address, city, state, zip, phone, email, password)
  
  # Login form
  def get_member_credentials(self):
    print()
    print("Member login")
    
    email = input("Email: ")
    password = input("Password: ")
    
    return MemberCredentials(email, password)
  
  def action_succeded(self, message):
    print()
    print(message + "has been done successfully!")
    input("Enter any key to continue")
  
class MemberData:
  def __init__(self, fname, lname, address, city, state, zip, phone, email, password):
    self.fname = fname
    self.lname = lname
    self.address = address
    self.city = city
    self.state = state
    self.zip = zip
    self.phone = phone
    self.email = email
    self.password = password

class MemberCredentials:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    