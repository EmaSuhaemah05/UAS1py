from core.baseapp import BaseApp
from view.view_book import ViewBook
from view.input_book import InputBook
from data_model.book import Book
class MainApp(BaseApp):
    def __init__(self):
        self.books = []
        self.InputBook =[]
        self.ViewBook = []
        BaseApp.__init__(self)



if __name__ == "__main__":
    app = MainApp()
    app.run()

@property
def list_book(self):
    return self.list_book
def add_book(self):
    return self.add_book()
