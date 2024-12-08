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
        title = input("Enter the book's title:\t")
        genre = input("Category:\t")
        
        if self.search_book(genre, title) :
            quantity =  int(input("Enter amount of books:\t"))
            cost = float(input("Price:\t$"))
            self.df_Book.loc[self.df_Book["Genre"] == genre, "Quantity"] += quantity
            self.df_Book.loc[self.df_Book["Genre"] == genre, "Price"] = cost
            
        else:
            author = input("Enter author name:\t")
            pYear = input("Published Year:\t")
            book_id = (input("Enter the book's ID:\t"))
            quantity =  int(input("Enter amount of books:\t"))
            cost = (input("Price:\t$"))
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
    def search_book(self, genre: str, title: str):
        # Filter books by Genre and Title (case-insensitive and whitespace-trimmed)
        matches = self.df_Book[
            (self.df_Book["Genre"].str.strip().str.lower() == genre.strip().lower()) &
            (self.df_Book["Title"].str.strip().str.lower() == title.strip().lower())
        ]
        if not matches.empty:
            self.print_book_matching(matches)
            return True
        print("No matching books found.")
        return False
    def print_book_matching(self, matches):
        print("Matching books:")
        print(matches[["Book_ID","Title", "Genre", "Quantity", "Price"]])

if __name__ == "__main__":
    book = Book()
    book.search_book("Classic","The Great Gatsby")
    