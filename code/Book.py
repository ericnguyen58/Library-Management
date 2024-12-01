import pandas as pd

class Book:
    def __init__(self,path = "./book.csv") -> None:
        self.path = path
        try:
            self.df_Book = pd.read_csv(self.path)
        except FileNotFoundError:
            # Create an empty DataFrame with the required columns
            self.df_Book = pd.DataFrame(columns=["Book_ID","Title",  "Quantity", "Price"])
            self.df_Book.to_csv(self.path, index=False)
    
    # Add new book and update old book quantity
    def add_book(self, title: str, book_ID: int, quantity: int, cost: float):
        if self.search_book(book_ID):
            self.df_Book.loc[self.df_Book["Book_ID"] == book_ID, "Quantity"] += quantity
            self.df_Book.loc[self.df_Book["Book_ID"] == book_ID, "Price"] = cost
        else:
            new_book = pd.DataFrame({"Book_ID": book_ID, "Title": title,  "Quantity":quantity, "Price": cost})
            self.df_Book = pd.concat([self.df_Book, new_book])
        self.df_Book.to_csv(self.path, index=False)
    
    # find book using ID and title
    def search_book(self, book_ID: int, title: str):
        self.df_Book = pd.read_csv(self.path)
        return book_ID in self.df_Book.Book_ID.values and title in self.df_Book.Title.values
        
    def print_df_user(self):
        self.df_user = pd.read_csv(self.path)
        print(self.df_user)    


