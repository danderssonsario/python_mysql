from enum import Enum

# Class responsible for serving menu and prompting user for input.
class Console:

  
  def main_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    return self.__prompt_for_input(len(options))
    

  def member_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    return self.__prompt_for_input(len(options))


  def subjects_menu(self, options):
    self.__print_options(options)
    return self.__prompt_for_input(len(options))

  def books_menu(self, no_of_books, books):
    print()
    print(f"""{no_of_books} books available on this subject""")
    print()
    for book in books:
      print (f"""Author: {book[1]}""")
      print (f"""Title: {book[2]}""")
      print (f"""ISBN: {book[0]}""")
      print (f"""Price: {book[3]}""")
      print (f"""Subject: {book[4]}""")
      print()


    print("Enter ISBN too add to Cart ")
    print("Press n + ENTER to continue browsing")
    print("Press ENTER to go back to menu")
    
    return input()
  
  
  def search_menu(self, title, options):
    self.__print_header(title)
    self.__print_options(options)
    return self.__prompt_for_input(len(options))
  
      
  def checkout_menu(self, checkout_data):
    print(checkout_data.items[0])
    print("Current Cart Contents: ")
    print("ISBN        Title                                                                             $    Qty   Total")
    print("-----------------------------------------------------------------------------------------------------")
    for item in checkout_data.items:
      print(f"""{item[1]}  {item[3]}{' ' * abs(80 - len(item[3]))}{item[4]}   {item[0]}    {item[0] * item[4]}""")
     # total_price = 0
    print("-----------------------------------------------------------------------------------------------------")
    print(f"""Total                                                                                                    ${checkout_data.total}""")
    print("-----------------------------------------------------------------------------------------------------")

    return input("Proceed to checkout (Y/N)?: ")
  
  def order_menu(self, order_data, cart):
    print()
    print(f"""                             Invoice for Order no. {order_data[0]}""")
    print("     Shipping Address")
    print(f"""     Name: {order_data[6]} {order_data[7]}""")
    print(f"""     Address: {order_data[2]}, {order_data[3]}, {order_data[4]}""")
    print(f"""     Address: {order_data[2]}, {order_data[3]}, {order_data[4]}""")
    print()
    print("     ISBN        Title                                                                             $    Qty   Total")
    print("-----------------------------------------------------------------------------------------------------")
    for item in cart.items:
      print(f"""{item[1]}  {item[3]}{' ' * abs(80 - len(item[3]))}{item[4]}   {item[0]}    {item[0] * item[4]}""")
     # total_price = 0
    print("-----------------------------------------------------------------------------------------------------")
    print(f"""Total                                                                                                    ${cart.total}""")
    print("-----------------------------------------------------------------------------------------------------")

    return input("Proceed to checkout (Y/N)?: ")

  def __print_header(self, title):
    print()
    print("***********************************************************")
    print("***               Online Book Store                     ***")
    print("                 " + title + "                       ")
    print("***                                                     ***")   
    print("***********************************************************") 

  def __print_options(self, options):
    print()
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}") 

  def __prompt_for_input(self, maxOptions):
    selectedOption = None
    while (selectedOption is None):
        choice = input("Enter choice: ")
            
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
    zip = input("Zip: ")
    phone = input("Phone: ")
    email = input("Email address: ")
    print()
    password = input("Enter a password: ")
    
    return MemberData(fname, lname, address, city, zip, phone, email, password)
  
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
    
  def get_search_string(self):
    print()
    return input("Enter your search: ")
  
  def get_quantity(self):
    print()
    return input("Enter quantity: ")
  
class MemberData:
  def __init__(self, fname, lname, address, city, zip, phone, email, password):
    self.fname = fname
    self.lname = lname
    self.address = address
    self.city = city
    self.zip = zip
    self.phone = phone
    self.email = email
    self.password = password

class MemberCredentials:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    