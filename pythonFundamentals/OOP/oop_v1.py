class Book:
    """fields: title, author, year, price"""

    # constructor with arguments
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    # returns details of Book object as a string
    def __str__(self):
        return "{0} ({1}) by {2} costs {3:1.2f}".format(self.title, self.year, self.author, self.price)

    # setter methods
    def setTitle(self, newTitle):
        self.title = newTitle

    def setAuthor(self, newAuthor):
        self.author = newAuthor

    def setYear(self, newYear):
        self.year = newYear

    def setPrice(self, newPrice):
        self.price = newPrice

    # getter methods
    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.price

    # test for equality, only 3 attributes are used here: title,


##    # author, year
##    def __eq__(self, other):
##        return self.getTitle().upper() == other.getTitle().upper() and \
##        self.getAuthor().upper() == other.getAuthor().upper() and \
##        self.getYear() == other.getYear()
##    
##    # these methods are for sorting
##    def __lt__(self, other):
##        return self.getPrice() < other.getPrice()
##
##    def __le__(self, other):
##        return self.getPrice() <= other.getPrice()
##
##
##blst = [Book('Basic Java', 'James', 2010, 20.45), \
##        Book('Python Programming', 'Jenny', 2009, 20.00), \
##        Book('C++', 'James', 2011, 15.0)]
##
##for p in sorted(blst):
##    print(p)
n1 = 10
n2 = 10
print(id(n1))
print(id(n2))

##b1 = Book(title="Python", author="Guido", year=2012, price=1000.00)
##b2 = Book(title="Python", author="Guido", year=2012, price=1000.00)
##
##print(b1 == b2)
##print(id(b1))
##print(id(b2))
