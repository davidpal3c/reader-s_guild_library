import os
import csv
from book import Book






def return_book():
    pass

# (menu option 3)
# •	Receives a book list
# •	Inputs an ISBN from the user and calls find_book_by_isbn()
# •	If an index to a matching book was returned and that book is currently borrowed, invokes the book’s return_it() method. Otherwise displays an appropriate message.



def add_book():
    pass

# (menu option 4)
# •	Receives a book list
# •	Inputs ISBN, title, author, and genre name from the user. 
# Genre name is validated – it must be one of the names listed earlier
# in the description of get_genre_name() – and translated into its integer
# value.
# •	Creates a new instance of Book and appends it to the list
   


def remove_book():
    pass
# (menu option 5)
# •	Receives a book list
# •	Inputs an ISBN from the user and calls find_book_by_isbn()
# •	If an index to a matching book was returned, removes the book from 
# the list. Otherwise displays an appropriate message.




def save_books():
    pass

# •	Receives a book list and pathname to a CSV file
# •	Iterates over the list, formatting a comma separated string 
# containing each book’s attribute values
# •	Writes each string as a separate line to the file
# •	Returns the number of books saved to the file


def find_book_by_isbn(books_lst, isbn_srch):
    
    for index, book in enumerate(books_lst):
        if book.get_isbn() == isbn_srch:
            return index
        
    return -1 


def borrow_book(books_lst):
    isbn_srch = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    # passes list of books and searc criteria to find_book_by_isbn(), and assigns returned index to variable
    foundB_index = find_book_by_isbn(books_lst, isbn_srch)
    
    if foundB_index == -1:
        print(f"{isbn_srch} not found in Database")
        return

    # Stores Book by index into variable
    foundBook = books_lst[foundB_index]

    # Checks availability and calls borrow_it() if available
    if foundBook.get_availability() == "Available":
        foundBook.borrow_it()
        print(f"{foundBook.get_title()} with ISBN {foundBook.get_isbn()} successfully borrowed.")

    else: 
        print(f"{foundBook.get_title()} with ISBN {foundBook.get_isbn()} is not currently available.")



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
        print()



def search_books(books_lst, search_str):
    
    search_lst = []
    for book in books_lst:
        if book.match_search(search_str):
            search_lst.append(book)

    print_books(search_lst)

    

def print_menu(menu_options, heading):
    
    print(heading)
    print(f"{"="*34}")
    for key, val in menu_options.items():
        print(key, val)



def load_books(books_lib_path, books_lst):
    
    with open(books_lib_path, 'r') as file:
        csv_reader = csv.reader(file)
        
        bCount = 0
        for line in csv_reader:
            isbn = line[0]
            title = line[1]
            author = line[2]
            genre = int(line[3])
            availability = line[4]

            # generates book object with indexed values of each line as its attributes
            book = Book(isbn, title, author, genre, availability)

            # adds book(s) object to books list 
            books_lst.append(book)

            bCount += 1

        print(f"\nBook catalog has been loaded \n(Number of books loaded {bCount})\n")
        return books_lst

        # for book in books_lst:
        #     print(book)
        

def main(): 

    print("Starting Library Management System...")

    input_path = input("Enter book catalog filename: ")
    books_lib_path = os.path.join(os.getcwd(), input_path)
    
    if not os.path.exists(books_lib_path):
        print(f"{input_path} does not exists - Exiting.")
        return
    
    else: 
        books_lst = []
        load_books(books_lib_path, books_lst)
        
        heading = "Reader's Guild Library - Main Menu"
        menu_options = {"1.": "Search for books", 
                        "2.": "Borrow a book",
                        "3.": "Return a book", 
                        "4.": "Add a book", 
                        "5.": "Remove a book", 
                        "6.": "Print catalog", 
                        "0.": "Exit the system"}

        while True: 
            
            print_menu(menu_options, heading)
            

            user_selection = input("Enter your selection: ").strip()

            match user_selection: 
                case '1': 
                    print("-- Search for books --")
                    search_str = input("Enter search value: ")
                    search_books(books_lst, search_str)

                case '2':
                    print("-- Borrow a book --")
                    borrow_book(books_lst)


                case '6':
                    print("-- Pring book catalog --")
                    search_lst = books_lst
                    print_books(search_lst)


                case '0':
                    exit()

                case _:
                    print("invalid input")



    # o	Call save_books() to save list of Books to file before
    #  ending the program

        
    # book_count = load_books(books_lib_path, books_lst)
    # print(f"Total books loaded: {book_count}")
    
    


if __name__ == "__main__":
    main()