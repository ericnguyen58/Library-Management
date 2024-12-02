from User import User
from Book import Book

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
            self.df_manage = pd.DataFrame(columns=["Name","Book_ID", "Transaction"])
            self.df_manage.to_csv(self.path, index=False)
    
    def borrowed_book(self,book_id,title,user_name):
        self.df_manage = pd.read_csv(self.path)
        self.book.df_Book = pd.read_csv(self.book.path)  
        self.user.df_user = pd.read_csv(self.user.path)                                     
        if self.book.search_book(book_id, title):
            transact = self.book.df_Book.loc[self.book.df_Book["Book_ID"] == book_id,"Price"].values[0]
            new_bill = pd.DataFrame([{"Name": user_name,"Book_ID":book_id,"Transaction":transact}])
            self.df_manage = pd.concat([self.df_manage,new_bill],ignore_index= True)
            self.df_manage.to_csv(self.path, index=False)
                
                
if __name__ == "__main__":
    library = Library()
    library.borrowed_book(1, "Python Programming" ,"john doe")
    library.borrowed_book(2, "Data Science 101" ,"jane smith")
    
    
        
        