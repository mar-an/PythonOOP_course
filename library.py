import pdb

class Library:

    def __init__(self, avialableBooks):
        self.avialableBooks = avialableBooks

    def displayAvialableBooks(self):
        i = 1
        print("___List of books___")
        for books in self.avialableBooks:
            print ("{}: {}".format(i,books))
            i+=1

    def lendBook(self, book):
        if (book in self.avialableBooks):
            self.avialableBooks.remove(book)
            print("Book '" +book+ "' has been lend!")
        else:
            print("Sorry requested book is not aviabalable")

    def addBook(self, book):
        self.avialableBooks.append(book)
        print("Book '" +book+ "' has been return!")

class Customer:

    def requestBook(self):
        print ("Type book you want to lend:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Type book you want to return:")
        self.book = input()
        return self.book

library = Library(['Komnata Tajemnic', 'Więzien Azkabanu', 'Kamien Filozoficzny', 'Czara Ognia'])
custometr = Customer()

while True:
    print()
    print("___Option list, type number 1..4___")
    print("1: displayAvialableBooks")
    print("2: requestBook")
    print("3: returnBook")
    print("4: exit")

    userChoice = int(input())

    if (userChoice == 1):
        library.displayAvialableBooks()
    elif (userChoice == 2):
        book = custometr.requestBook()
        library.lendBook(book)
    elif (userChoice == 3):
        book = custometr.returnBook()
        library.addBook(book)
    elif (userChoice == 4):
        quit()
