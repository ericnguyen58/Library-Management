from User import *
from Book import *
import pandas as pd
class Library:
    def __init__(self, path = "./Manage.csv"):
        self.path = path
        self.user = User()
        self.book = Book()
        self.borrow_book = []
        try:
            self.df_manage = pd.read_csv(self.path)
        except:
            self.df_manage = pd.DataFrame(columns=["User_ID","Borrow_book", "Transaction"])
            self.df_manage.to_csv(self.path, index=False)
    
    def borrowed_book(self,book_id, title):
        self.df_manage = pd.read_csv(self.path)
        self.book.df_Book = pd.read_csv(self.book.path)  
        self.user.df_user = pd.read_csv(self.user.path)                                     
        if self.book.search_book(title, book_id):
            book_row = self.book.df_Book.loc[(self.book.df_Book["Book_ID"] == book_id) & 
                                             (self.book.df_Book["Title"] == title)]
            print(book_row)
        else:
            
            print("Book not found")
                
                
test = Library()
test.borrowed_book(112, "Python Programming")
            
        
        