import json
from logging import exception
class LibraryManagementSystem:
    borrowed =[]

    def __init__(self, user):
        self.user =  user
        self.borrowed = []


    def add_new_book(self, title, author, quantity):
        self.id = 0
        self.title = title 
        self.author = author
        self.quantity = quantity
        self.book_data = {}
        try :
            with open ("book.txt", "r") as file:
                content = file.readlines()
        
        except FileNotFoundError:
            content = []
        
        if len(content) == 0:
            id = 1
            self.book_data = {"id": id, "title": self.title, "author": self.author, "quantity": self.quantity}

        else:
            last_line = content[-1]
            data_dict = json.loads(last_line)
            id = data_dict.get("id", 0) + 1
            self.book_data = {"id": id, "title": self.title, "author": self.author, "quantity": self.quantity}
        with open("book.txt", "a") as file:
            file.write(json.dumps(self.book_data)+"\n")
            print("book added successfully")

    

    def borrow_book(self,title, author):
        self.title = title
        self.author = author
        self.updated_content = []
        self.book_found = False        
        try :
            with open ("book.txt", "r") as file:
                content = file.readlines()
        
        except FileNotFoundError:
             content = []

        if len(content) == 0:
            print("No books available")
        
        elif len(content) > 0:
            for i in content:
                j = json.loads(i)
                try :
                    if j.get("title") == self.title:
                    
                        self.book_found = True
                        if j.get("quantity") == 0:
                            print("book is out of stock")
                        else:
                            j["quantity"] -= 1
                            self.borrowed.append(self.title)
                            self.updated_content.append(j)
                            print(f"book {self.title} borrowed successfully")
                    else:
                        self.updated_content.append(j)

                except KeyError:
                        print("book not found")
                    
        if not self.book_found:
            print(f"book \"{self.title}\" not found")
        
        else:
            with open("book.txt", "w") as file:
                for i in self.updated_content:
                    print(i)
                    file.write(f"""{json.dumps(i)}\n""")
        

    def return_book(self, title, author):
        self.title = title
        self.author = author
        self.updated_content = []
        print(self.borrowed)
        print(self.title)
        for item in self.borrowed:
            if item == self.title:
                self.borrowed.remove(self.title)
                print(self.borrowed)
                
                with open("book.txt", "r") as file:
                    content = file.readlines()
                    for i in content:
                        print("i",i)
                        j = json.loads(i)
                        print("j",j)
                        for key, value in j.items():
                            if key == "title" and value == self.title:
                                j["quantity"] += 1
                                self.updated_content.append(j)
                            elif key == "title" and value != self.title:
                                self.updated_content.append(j)
                    with open("book.txt", "w") as file:
                        for i in self.updated_content:
                            print("updated content",i)
                            file.write(f"""{json.dumps(i)}\n""")
                            print(f"{self.title} returned successfully")
        print(f"{self.title} not borrowed by you")
                
        with open("book.txt", "w") as file:
            for i in self.updated_content:
                file.write(f"""{json.dumps(i)}\n""")
                print("quantity updated successfully")
        
        
                         
       
    def view_borrowed_books(self):
        if len(self.borrowed) == 0:
            print("No books borrowed")
        else:
            print(f"Borrowed books: {self.borrowed}")

    def view_books(self):
        with open("book.txt", "r") as file:
            content =file.readlines()
            for i in content:
                j = json.loads(i)
                print(f"ID: {j['id']}, Title: {j['title']}, Author: {j['author']}, Quantity: {j['quantity']}")
            


u1 = LibraryManagementSystem("Monika")
# u1.add_new_book("Multithreading", "charley", 12)
# u1.add_new_book("data structures", "hakuna", 12)
# u1.add_new_book("computer science", "dr. mohan", 12)
# u1.view_books()

u1.borrow_book("Times", "John Doe")
# u1.borrow_book("computer science", "dr. mohan")
u1.borrow_book("data structures", "hakuna")

# u1.return_book("data structures", "hakuna")
# u1.view_borrowed_books()
# u1.return_book("computer science", "dr. mohan")
# u1.return_book("Times", "John Doe")







        

