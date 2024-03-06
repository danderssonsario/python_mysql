# from model.database import Database
from bookstore import BookStore
from console import Console
from controller import Controller

# db = Database("", "")


def main():
    
    view = Console()
    model = BookStore()
    controller = Controller(view, model)
    
    controller.run()

if __name__ == "__main__":
    main()
