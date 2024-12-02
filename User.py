import pandas as pd
class User:
    def __init__(self, path = "./member.csv" ):
        self.path = path
        self.Borrow_book = []
        try:
            self.df_user = pd.read_csv(self.path)
        except:
            self.df_user = pd.DataFrame(columns=["User_ID","Name","Email"])
            self.df_user.to_csv(self.path, index=False)
            
    #add member
    def add_member(self):
        if self.df_user.empty:
            new_ID = 1000
        else:
            # Get the max User_ID and increment it
            new_ID = self.df_user["User_ID"].max() + 1
        
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        # Create a new user entry as a DataFrame
        new_user = pd.DataFrame([{
            "User_ID": new_ID,
            "Name": name,
            "Email": email,
            "Borrow_book": None
        }])

        # Concatenate and save
        self.df_user = pd.concat([self.df_user, new_user], ignore_index=True)
        self.df_user.to_csv(self.path,index = False)
        
    #Return True if ID is in df_user, False otherwise   
    def search_user(self, ID):
        self.df_user = pd.read_csv(self.path)
        return ID in self.df_user.User_ID.values
     
    def remove_user(self):
        while True:
            try:
                ID = int(input("Enter the User ID you want to remove: "))
                break
            except:
                pass
        if self.search_user(ID):
            self.df_user = self.df_user[self.df_user["User_ID"] != ID]
            self.df_user = self.df_user.to_csv(self.path,index = False)
        else:
            print("User ID not found")

    def print_df_user(self):
        self.df_user = pd.read_csv(self.path)
        print(self.df_user)
    

if __name__ == "__main__":
    user = User()
    user.add_member()
    user.add_member()
    user.print_df_user()
    user.remove_user()
    user.print_df_user()