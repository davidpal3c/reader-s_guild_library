# Reader's Guild Library program (library management system)
# Program incorporating library management functionality with features:
# Search book, Borrow book, Return book, Add book (to catalog), Remove book, Print Catalog, and i/o file handling. 
# The program incorporates a class constructor to generate book objects, handle functionality through the given methods, 
# and construct book objects with attributes used such as: isbn, title, author, genre, and availability. 
# books.py and books.csv are included along side with the main program file (main.py)
# Date: 2024-03-27



import os
import csv
from book import Book

# constant variables declared for admin password, headings and menu options
ADMIN_PASS = "2130"


HEADING = "Reader's Guild Library - Main Menu"
MAIN_MENU = {"1.": "Search for books", 
                "2.": "Borrow a book",
                "3.": "Return a book", 
                "0.": "Exit the system"}


L_HEADING = "Reader's Guild Library - Librarian Menu"
L_MENU = {"1.": "Search for books", 
                "2.": "Borrow a book",
                "3.": "Return a book", 
                "4.": "Add a book", 
                "5.": "Remove a book", 
                "6.": "Print catalog", 
                "0.": "Exit the system"}



# Removes book from books_list 
def remove_book(books_lst, books_lib_path):
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()

    # Passes isbn search string to search helper function and receives book index or -1 if not found
    foundB_index = find_book_by_isbn(books_lst, isbn_srch)

    # Assigns indexed book object to variable
    foundBook = books_lst[foundB_index]

    # condition statement to remove book if available, or state whether it hasnt been return, or if it is not found  
    if foundB_index == -1:
        print(f"No book found with isbn: {isbn_srch}")
        return
    
    elif foundBook.get_availability() != "Available":
        print(f"'{foundBook.get_title()}' with ISBN {foundBook.get_isbn()} has been borrowed and needs to be returned first.")
    
    else: 
        books_lst.pop(foundB_index)
        print(f"'{foundBook.get_title()}' with ISBN {foundBook.get_isbn()} successfully removed.")

    save_books(books_lst, books_lib_path)



# Adds a book to list, validates genre input
def add_book(books_lst, books_lib_path):
    
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()
    title = input("Enter title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    availability = True

    # takes entered new book info and passes it to the object constructor in class
    validator = Book(isbn, title, author, genre, availability)


    # validates whether book meets genre category requirement, and prints entered book info.
    while True: 

        if validator.validate_genre(genre) == True:
            genre = input("Invalid genre. Choices are: \nRomance, Mystery, Science Fiction, Thriller, \nYoung Adult, Children's Fiction, Self-help,\nFantasy, Historical Fiction, Poetry \nEnter genre: ")
        
        else: 
            print(f"'{validator.get_title()}' with ISBN {validator.get_isbn()} successfully added.\
                  {validator.get_genre()} {validator.get_availability()}")
            break
        
    # adds new book object to list of books 
    books_lst.append(validator)

    # returns updated list of books and file path to save book helper function to save changes to file
    save_books(books_lst, books_lib_path)


# Saves changes to file
def save_books(books_lst, books_lib_path):
    
    write_lst = []
    countB = 0

    # Takes attribute values for each book object and adds them to list line by line
    for book in books_lst:
        isbn = book.get_isbn()
        title = book.get_title()
        author = book.get_author()
        genre = book.get_genre()
        availability = book.get_avail()
        countB += 1 

        line = [isbn, title, author, genre, availability]
        
        # lineW = ','.join(map(str, line))
        write_lst.append(line)

    # Opens file in write mode, and re-writes row by row from the new 'updated' list
    with open(books_lib_path, 'w', newline="") as lib_file:
        csv_writer = csv.writer(lib_file)

        for row in write_lst:
            csv_writer.writerow(row)

    return countB

# Returns book marking availability to True 
def return_book(books_lst):
        
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()

    foundB_index = find_book_by_isbn(books_lst, isbn_srch)
    
    # Uses index value check if books is found 
    if foundB_index == -1:
        print(f"No book found with isbn: {isbn_srch}")
        return

    foundBook = books_lst[foundB_index]

    # Checks availability and calls return_it() if 'borrowed', to change book instance availability to True (Returned/Available)
    if foundBook.get_availability() == "Borrowed":
        foundBook.return_it()
        print(f"'{foundBook.get_title()}' with ISBN {isbn_srch} was successfully returned")

    else:
        print(f"'{foundBook.get_title()}' with ISBN {isbn_srch} hasn't been borrowed!")


# Finds book object using isbn
def find_book_by_isbn(books_lst, isbn_srch):
    
    for index, book in enumerate(books_lst):
        if book.get_isbn() == isbn_srch:
            return index
        
    return -1 

# Borrows book using helper function(isbn) to find book object and changes availability to false
def borrow_book(books_lst):
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()

    # passes list of books and searc criteria to find_book_by_isbn(), and assigns returned index to variable
    foundB_index = find_book_by_isbn(books_lst, isbn_srch)
    
    # Uses index value check if books is found 
    if foundB_index == -1:
        print(f"No book found with isbn: {isbn_srch}")
        return

    # Stores Book by index into variable
    foundBook = books_lst[foundB_index]

    # Checks availability and calls borrow_it() if available, to change book instance availability to False (book borrowed)
    if foundBook.get_availability() == "Available":
        foundBook.borrow_it()
        print(f"'{foundBook.get_title()}' with ISBN {foundBook.get_isbn()} successfully borrowed.")

    else: 
        print(f"'{foundBook.get_title()}' with ISBN {foundBook.get_isbn()} is not currently available.")


# Formats string display and prints catalogue
def print_books(search_lst):
    
    if not search_lst:
        print("No books found matching the search criteria.")
        return
    
    # Format strings for catalog display
    print("{:15s} {:26s} {:27s} {:21s} {:s}".format("ISBN", "Title",
    "Author", "Genre", "Availability"))
    print("{:15s} {:26s} {:27s} {:21s} {:s}".format("-"*15,"-"*26, "-"*27, "-"*21, "-"*12))

    # Uses str format in book class to display each object
    for book in search_lst:
        book_str = str(book)
        print(book_str)
   

# Searches for book (isbn, title, author, and genre)
def search_books(books_lst, search_str):
    
    search_lst = []

    # Matches search string with every book object using search method inside of class
    for book in books_lst:
        if book.match_search(search_str):
            search_lst.append(book)

    print_books(search_lst)

    
# Displays main menu depending on authentication status
def print_menu(MAIN_MENU, HEADING, L_MENU, L_HEADING, admin):

    
    menu = L_MENU if admin else MAIN_MENU 

    print(L_HEADING if admin else HEADING)
    print(f"{"="*34}")
   
    for key, val in menu.items():
        print(key, val)
   
    print()


# Loads books from file into list
def load_books(books_lib_path, books_lst):
    
    # Opens file in read mode
    with open(books_lib_path, 'r') as lib_file:
        csv_reader = csv.reader(lib_file)
        
        bCount = 0

        # Parses value by index per line, and assings to local variable(s) for each book
        for line in csv_reader:
            isbn = line[0]
            title = line[1]
            author = line[2]
            genre = int(line[3])
            availability = line[4]

            # generates book object with indexed values in variables for each line (book) as attributes
            book = Book(isbn, title, author, genre, availability)

            # adds book object to books list 
            books_lst.append(book)

            bCount += 1


        print(f"Book catalog has been loaded \n(Number of books loaded {bCount})\n")
        return books_lst

        


# Management function for the entire program
def main(): 

    print("Starting the system...")

    input_path = ""
    while input_path == "" or (not os.path.exists(books_lib_path)):
        input_path = input("Enter book catalog filename: ")
        books_lib_path = os.path.join(os.getcwd(), input_path)
        
        if not os.path.exists(books_lib_path):
            print("File not found. ")
    
    books_lst = []
    load_books(books_lib_path, books_lst)


    admin = False

    # Menu functionality iteration working as a global management selection display: 
    while True: 
        
        print_menu(MAIN_MENU, HEADING, L_MENU, L_HEADING, admin)
        
        user_selection = input("Enter your selection: ").strip()

        # Evaluates user selection and executes task accordingly:        
        if user_selection == '1': 
            print("-- Search for books --")
            search_str = input("Enter search value: ")
            search_books(books_lst, search_str)

        elif user_selection == '2':
            print("-- Borrow a book --")
            borrow_book(books_lst)

        elif user_selection == ADMIN_PASS:
            admin = True
            print_menu(MAIN_MENU, HEADING, L_MENU, L_HEADING, admin)

        elif user_selection == '3':
            print("-- Return Book --")
            return_book(books_lst)

        elif user_selection == '4' and admin == True:
            print("-- Add a book --")
            add_book(books_lst, books_lib_path)

        elif user_selection == '5' and admin == True:
            print("-- Remove a book --")
            remove_book(books_lst, books_lib_path)

        elif user_selection == '6' and admin == True:
            print("-- Pring book catalog --")
            search_lst = books_lst
            print_books(search_lst)

        elif user_selection == '0':
            print(f"(Number of books saved to file: {save_books(books_lst, books_lib_path)})\n")
            print("-- Exit the system -- \nBook catalog has been saved. \nGood Bye!\n")
            exit()

        else: 
            print("Invalid option")



if __name__ == "__main__":
    main()