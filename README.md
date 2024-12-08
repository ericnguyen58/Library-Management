Library Management System using Pandas

A simple Library Management System (LMS) built using Pandas in Python. This system allows users to borrow and return books,
and keeps track of transactions. It manages books, users, and transaction records with easy-to-understand functionality.

Features

Books Management: List of books with details such as title, author, genre, and available copies.
Users Management: Track users with unique IDs, names, and other personal details.
Transaction Management: Record borrowing and returning of books by users.
Borrowing Books: Users can borrow books if they are available in the library.
Returning Books: Users can return borrowed books and update the library's inventory.

How to Install
1. Clone the repostory :
   git clone https://github.com/ericnguyen58/Library-Management.git
2. Dowload essential library:
   pip install -r requirements.txt

Usage

Data Structure 
-Book: A dataframe that contains information about the books in the library
  -Columns: Book_ID,Title,Author,Genre,Published Year,Available,Quantity,Price
-User: A dattaframe that contains user information 
  -Columns: User_ID,Name,Email,Phone,Address
-Library: A dataframe that tracks and manage the transaction
  -Columns: Transaction_ID,User_ID,User Name,Book_ID,Title,State,Price

Example Usage:




