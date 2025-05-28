class Library:
    def __init__(self):
        self.catalog = {}
        self.deleted = []
        self.borrowed = {}

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.catalog[title] = new_book

    def remove_book(self, title):
        if title in self.catalog:
            self.deleted.append(self.catalog.pop(title))
            print(f"You successfully removed '{title}' from the catalog.")
        else:
            print(f"Book '{title}' not found in catalog.")

    def list_books(self): # list available books
        for key in self.catalog.keys():
            book = self.catalog[key]
            if book.available:
                print(f"'{book.title}' by {book.author}")
    
    def borrow_book(self, title):
        if title in self.catalog:
            book = self.catalog[title]
            book.check_out()
            if book.available == False:
                self.borrowed[title] = book
        else:
            print(f"'{title}' is not in our system.")
                
    def return_book(self, title):
        if title in self.catalog:
            book = self.catalog[title]
            book.check_in()
            if book.available == True:
                if title in self.borrowed:
                    self.borrowed.pop(title)
        else:
            print(f"'{title}' is not in our system.")

    def list_borrowed(self):
        for key in self.borrowed.keys():
            book = self.borrowed[key]
            print(book)