import pandas as pd

class Book:
    def __init__(self,path = "book.csv") -> None:
        self.path = path
        try:
            self.df_Book = pd.read_csv(self.path)
        except FileNotFoundError:
            # Create an empty DataFrame with the required columns
            self.df_Book = pd.DataFrame(columns=["Book_ID","Title","Author" , "Genre", "Published Year","Availabe",  "Quantity", "Price"])
            self.df_Book.to_csv(self.path, index=False)
    
    # Add new book and update old book quantity
    def add_book(self):
        book_id = int(input("Enter the book's ID:\t"))
        title = input("Enter the book's title:\t")
        quantity =  int(input("Enter amount of books:\t"))
        cost = float(input("Price:\t$"))
        if self.search_book(book_id, title) :
            
            self.df_Book.loc[self.df_Book["Book_ID"] == book_id, "Quantity"] += quantity
            self.df_Book.loc[self.df_Book["Book_ID"] == book_id, "Price"] = cost
            self.df_Book.loc[self.df_Book["Book_ID"] == book_id, "Available"] = True
            
        else:
            author = input("Enter author name:\t")
            genre = input("Category:\t")
            pYear = input("Published Year:\t")
            is_avai = quantity > 0

            new_book = pd.DataFrame([{"Book_ID": book_id,
                                      "Title": title, 
                                      "Author" : author,
                                      "Genre" : genre,
                                      "Published Year" : pYear,
                                      "Available" : is_avai,
                                      "Quantity":quantity, 
                                      "Price": cost
                                      }])
            
            self.df_Book = pd.concat([self.df_Book, new_book], ignore_index=True)
        self.df_Book.to_csv(self.path, index=False)
    
    # find book using ID and title
    def search_book(self, book_ID: int, title):
        self.df_Book = pd.read_csv(self.path)
        if title not in self.df_Book.loc[self.df_Book["Book_ID"] == book_ID,"Title"].values:
            return False
        if self.df_Book.loc[self.df_Book["Book_ID"] == book_ID,"Quantity"].values[0] > 0:
            return True
        return False
            
           
        
if __name__ == "__main__":
    book = Book()
    book.add_book()
    
