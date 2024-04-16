import os
import csv
from book import Book



# Removes book from books_list 
def remove_book(books_lst, books_lib_path):
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()

    foundB_index = find_book_by_isbn(books_lst, isbn_srch)
    foundBook = books_lst[foundB_index]

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

    validator = Book(isbn, title, author, genre, availability)

    while True: 

        if validator.validate_genre(genre) == True:
            genre = input("Invalid genre. Choices are: \nRomance, Mystery, Science Fiction, Thriller, \nYoung Adult, Children's Fiction, Self-help,\nFantasy, Historical Fiction, Poetry \nEnter genre: ")
        
        else: 
            print(f"'{validator.get_title()}' with ISBN {validator.get_isbn()} successfully added.\
                  {validator.get_genre()} {validator.get_availability()}")
            break
        
    books_lst.append(validator)

    save_books(books_lst, books_lib_path)


# Saves changes to file
def save_books(books_lst, books_lib_path):
    
    write_lst = []
    countB = 0
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


    with open(books_lib_path, 'w', newline="") as lib_file:
        csv_writer = csv.writer(lib_file)

        for row in write_lst:
            csv_writer.writerow(row)

    return countB

# Returns book marking availability to True 
def return_book(books_lst):
        
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ").strip()

    foundB_index = find_book_by_isbn(books_lst, isbn_srch)
    
    if foundB_index == -1:
        print(f"No book found with isbn: {isbn_srch}")
        return

    foundBook = books_lst[foundB_index]

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
    
    if foundB_index == -1:
        print(f"No book found with isbn: {isbn_srch}")
        return

    # Stores Book by index into variable
    foundBook = books_lst[foundB_index]

    # Checks availability and calls borrow_it() if available
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
    

    print("{:15s} {:26s} {:27s} {:21s} {:s}".format("ISBN", "Title",
    "Author", "Genre", "Availability"))
    print("{:15s} {:26s} {:27s} {:21s} {:s}".format("-"*15,"-"*26, "-"*27, "-"*21, "-"*12))

    for book in search_lst:
        book_str = str(book)
        print(book_str)
   

# Searches for book (isbn, title, author, and genre)
def search_books(books_lst, search_str):
    
    search_lst = []
    for book in books_lst:
        if book.match_search(search_str):
            search_lst.append(book)

    print_books(search_lst)

    
# Displays main menu 
def print_menu(main_menu, heading, l_menu, l_heading, admin):
            
    if admin:  
        print(f"\n{l_heading}")
        print(f"{"="*34}")
        for key, val in l_menu.items():
            print(key, val)
    
    else:
        print(f"\n{heading}")
        print(f"{"="*34}")
        for key, val in main_menu.items():
            print(key, val)




# Loads books from file into list
def load_books(books_lib_path, books_lst):
    
    with open(books_lib_path, 'r') as lib_file:
        csv_reader = csv.reader(lib_file)
        
        bCount = 0
        for line in csv_reader:
            isbn = line[0]
            title = line[1]
            author = line[2]
            genre = int(line[3])
            availability = line[4]

            # generates book object with indexed values of each line as attributes
            book = Book(isbn, title, author, genre, availability)

            # adds book objects to books list 
            books_lst.append(book)

            bCount += 1

        print(f"\nBook catalog has been loaded \n(Number of books loaded {bCount})")
        return books_lst

        


# Management function in charge of 
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

    while True: 
        
        heading = "Reader's Guild Library - Main Menu"
        main_menu = {"1.": "Search for books", 
                        "2.": "Borrow a book",
                        "3.": "Return a book", 
                        "0.": "Exit the system"}


        l_heading = "Reader's Guild Library - Librarian Menu"
        l_menu = {"1.": "Search for books", 
                        "2.": "Borrow a book",
                        "3.": "Return a book", 
                        "4.": "Add a book", 
                        "5.": "Remove a book", 
                        "6.": "Print catalog", 
                        "0.": "Exit the system"}
        
        print_menu(main_menu, heading, l_menu, l_heading, admin)
        
        user_selection = input("Enter your selection: ").strip()


        match user_selection: 
            case '1': 
                print("-- Search for books --")
                search_str = input("Enter search value: ")
                search_books(books_lst, search_str)

            case '2':
                print("-- Borrow a book --")
                borrow_book(books_lst)

            case '2130':
                admin = True
                print_menu(main_menu, heading, l_menu, l_heading, admin)

            case '3':
                print("-- Return Book --")
                return_book(books_lst)

            case '4':
                print("-- Add a book --")
                add_book(books_lst, books_lib_path)


            case '5':
                print("-- Remove a book --")
                remove_book(books_lst, books_lib_path)

            case '6':
                print("-- Pring book catalog --")
                search_lst = books_lst
                print_books(search_lst)


            case '0':
                print(f"(Number of books saved to file: {save_books(books_lst, books_lib_path)})\n")
                print("-- Exit the system -- \nBook catalog has been saved. \nGood Bye!\n")
                exit()

            case _:
                print("Invalid option")



if __name__ == "__main__":
    main()