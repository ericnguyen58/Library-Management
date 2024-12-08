from User import User
from Book import Book

import pandas as pd
import numpy as np
class Library:
    def __init__(self, path = "Manage.csv"):
        self.path = path
        self.user = User()
        self.book = Book()
        self.borrow_book = []
        try:
            self.df_manage = pd.read_csv(self.path)
        except:
            self.df_manage = pd.DataFrame(columns=["Transaction_ID","User_ID","User Name","Book_ID","Title","Borrow_book_ID", "Transaction"])
            self.df_manage.to_csv(self.path, index=False)

    def borrowed_book(self,genre, title):
        if self.book.search_book(genre, title):
            pass        



                
                #hello
if __name__ == "__main__":
    library = Library()
    print(library.book.search_book("Fantasy","J.R.R Tolkien"))
