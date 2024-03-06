# from model.database import Database
from BookStore import BookStore
from Console import Console
from Controller import Controller

# db = Database("", "")


def main():
    view = Console()
    model = BookStore()
    controller = Controller(view, model)
    
    controller.run()

if __name__ == "__main__":
    main()
