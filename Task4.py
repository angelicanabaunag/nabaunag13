class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: {self.title} by {self.author} ({self.year_published})")

# Create three book objects
book1 = Book("Heartless", "Jonaxx Stories", 2013)
book2 = Book("Twisted Love", "Ana Huang",  2021)
book3 = Book("The Fine Print", "Loren Asher", 2021)

# Display book details
book1.describe()
book2.describe()
book3.describe()
