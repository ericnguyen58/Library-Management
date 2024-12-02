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
        if not self.book.search_book(book_id, title):
            print(f"Book {title} not found")
            return
        if user_name in self.df_manage["Name"].values:
            print(1)
            current_bill = self.df_manage.loc[self.df_manage["Name"] == user_name, "Transaction"].values[0]
            new_transaction = self.book.df_Book.loc[self.book.df_Book["Book_ID"] == book_id,"Price"].values[0]
            self.df_manage.loc[self.df_manage["Name"] == user_name] = current_bill + new_transaction
        else:
            print(2)
            transact = self.book.df_Book.loc[self.book.df_Book["Book_ID"] == book_id,"Price"].values[0]
            new_bill = pd.DataFrame([{"Name": user_name,"Book_ID":book_id,"Transaction":transact}])
            self.df_manage = pd.concat([self.df_manage,new_bill],ignore_index= True)
        self.book.df_Book.loc[self.book.df_Book["Book_ID"]== book_id ,"Quantity"] -= 1
        self.book.df_Book.to_csv(self.book.path, index= False)
        self.df_manage.to_csv(self.path, index=False)



                
                
if __name__ == "__main__":
    library = Library()
    library.borrowed_book(1, "Python Programming" ,"mark jones")
    library.borrowed_book(2, "Data Science 101" ,"jane smith")
    
    
        
        