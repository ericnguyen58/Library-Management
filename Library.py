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
            self.df_manage = pd.DataFrame(columns=["Name","Borrow_book_ID", "Transaction"])
            self.df_manage.to_csv(self.path, index=False)
    
    def borrowed_book(self):
        customer = input("Enter your name:\t")
        title = input("Enter the book you want to borrow: \t")
        
        if title in self.book.search_book()
        self.df_manage = pd.read_csv(self.path)
        self.book.df_Book = pd.read_csv(self.book.path)  
        self.user.df_user = pd.read_csv(self.user.path)  
        if not self.book.search_book(book_id, title):
            print(f"Book {title} not found")
            return
        borrow_list = [book_id]
        if not user_name in self.df_manage["Name"].values:
            transact = self.book.df_Book.loc[self.book.df_Book["Book_ID"] == book_id,"Price"].values[0]
            new_bill = pd.DataFrame([{"Name": user_name,"Borrow_book_ID":book_id,"Transaction":transact}])
            self.df_manage = pd.concat([self.df_manage,new_bill],ignore_index= True)
        else:
            # temp = self.df_manage.loc[self.df_manage["Name"] == user_name,"Borrow_book_ID"].values[0]      
            # temp = np.append(temp, book_id)

            # list_temp = temp.tolist()
            # self.df_manage.loc[self.df_manage["Name"] == user_name,"Borrow_book_ID"] = [list_temp]
            
            current_bill = self.df_manage.loc[self.df_manage["Name"] == user_name, "Transaction"].values[0]
            new_transaction = self.book.df_Book.loc[self.book.df_Book["Book_ID"] == book_id,"Price"].values[0]
            self.df_manage.loc[self.df_manage["Name"] == user_name,"Transaction"] = current_bill + new_transaction
            
            
            
        self.book.df_Book.loc[self.book.df_Book["Book_ID"]== book_id ,"Quantity"] -= 1
        self.book.df_Book.to_csv(self.book.path, index= False)
        self.df_manage.to_csv(self.path, index=False)



                
                #hello
if __name__ == "__main__":
    library = Library()
    library.borrowed_book(6,"Blah Bla", "loi nguyen")
    
    
    
    
    
        
        