from User import User
from Book import Book

import pandas as pd
import numpy as np
class Library:
    def __init__(self, path = "Manage.csv"):
        self.path = path
        self.user = User()
        self.book = Book()

        try:
            self.df_manage = pd.read_csv(self.path)
        except:
            self.df_manage = pd.DataFrame(columns=["Transaction_ID","User_ID","User Name","Book_ID","Title", "State","Price"])
            self.df_manage.to_csv(self.path, index=False)

    def borrowed_book(self,genre, title,user_name,user_id):
        if self.book.search_book(genre, title):
            data = self.book.df_Book.loc[
                (self.book.df_Book["Genre"] == genre) & (self.book.df_Book["Title"] == title),
                ["Book_ID", "Price"]
            ].values[0]
        
        if not self.user.search_user(user_id,user_name):
            self.user.add_member()
        
        process = pd.DataFrame([{
            "Transaction_ID": self.df_manage.shape[0]+1,
            "User_ID": user_id,
            "User Name": user_name,
            "Book_ID": data[0],
            "Title": title,
            "State": "Borrowed",
            "Price": data[1],
        }])
        
        self.df_manage = pd.concat([self.df_manage,process],ignore_index=True)
        self.df_manage.to_csv(self.path,index= False)
        print()
        
    def return_book(self):
        if self.df_manage.shape[0] == 0:
            print("No transaction to return")
            return
        user_name = input("Enter your name:\t")
        user_id = int(input("Enter your ID:\t"))
        if self.search(user_name,user_id):
            transact_ID = int(input("Enter transact ID you want to process: \t"))
            transact = self.df_manage[(self.df_manage["Transaction_ID"] == transact_ID) 
                                              & (self.df_manage["State"] == "Borrowed")]
            if not transact.empty:
                self.df_manage.loc[self.df_manage["Transaction_ID"] == transact_ID,
                                   ["State","Price"]] = ["Returned",0.0]
                print("Returned successfully")
                self.df_manage.to_csv(self.path,index=False)
            else:
                print("Transaction not found or book returned already")
        
        

    def search(self,user_name,user_id:int):
        matching = self.df_manage[(self.df_manage["User_ID"] == user_id) &
                        (self.df_manage["User Name"] == user_name)]
        if matching.empty:
            print("No record found")
            return False
        print(matching)
        return True
    
        # if not matching.empty:
if __name__ == "__main__":
    library = Library()
    # library.borrowed_book("Fiction","To Kill a Mockingbird","Eric Toan",1000)
    library.return_book()
