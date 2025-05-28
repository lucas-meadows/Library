class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.year = None
        self.publisher = None
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.author}."

    def add_year(self, year):
        self.year = year

    def add_publisher(self, publisher):
        self.publisher = publisher

    def return_details(self):
        print(f"'{self.title}', {self.author}, {self.year}, {self.publisher}")

    def check_out(self):
        if self.available:
            self.available = False
            print(f"You have checked out'{self.title}'.")
        else:
            print(f"'{self.title}' is already checked out")
            
    def check_in(self):
        if self.available == False:
            self.available = True
            print(f"You have checked in '{self.title}'.")
        else:
            print(f"'{self.title}' has already been checked in.")