import os
import csv
from book import Book



def find_book_by_isbn():
    pass

# •	Receives a book list and an ISBN
# •	Iterates through the list of books and compares the ISBN parameter to each book’s isbn. Iteration stops when an exact match is found or when the end of the list is reached.
# •	Returns the index of the matching book or -1 if none found




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




def borrow_book():
    pass

# (menu option 2)
# •	Receives a book list
# •	Inputs an ISBN from the user and calls find_book_by_isbn()
# •	If an index to a matching book was returned and that book 
# is currently available, invokes the book’s borrow_it() method. 
# Otherwise displays an appropriate message.


def print_books(search_lst):
    
    if search_lst:
        print("Matching Books:")
    else:
        print("No books found matching the search criteria.")
        return

    for book in search_lst:
        print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}\n")
    
# (menu option 6, 1)
# •	Receives a book list
# •	Displays a book information heading, then iterates through the book list displaying each Book object on a separate line




def search_books(books_lst, search_str):
    
    # search = [book for book in books_lst if Book.get_title(search_str)]

    search_lst = []
    for book in books_lst:
        if book.match_search(search_str):
            search_lst.append(book)

    print_books(search_lst)

    

# •	Iterates through the list of books and checks if the search string 
# appears in isbn, title, author, or genre name. If any match is found, 
# the book is added to the search result list.

# •	Returns search result list
# •	After calling this function, call print_books() passing to it the 
# search result list




def print_menu(menu_options, heading):
    
    print(heading)
    print(f"{"="*34}")
    for key, val in menu_options.items():
        print(key, val)

# •	Displays the heading and menu options passed in
# •	Inputs selection from user until valid selection is entered
# •	Returns user’s valid selection


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
        

# •	Receives an empty list and pathname to an existing CSV file
# •	Iterates over each line (i.e. book) in the file, parsing the
#  attribute values into separate variables
# •	Creates Book objects from each set of attributes and adds them
#  one-by-one onto the list
# •	Returns the number of books loaded

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
        menu_options = {"1.": "Search for books", "2.": "Borrow a book", "3.": "Return a book", "0.": "Exit the system"}

        while True: 
            
            print_menu(menu_options, heading)
            

            user_selection = input("Enter your selection: ").strip()

            match user_selection: 
                case '1': 
                    print("-- Search for books --")
                    search_str = input("Enter search value: ")
                    search_books(books_lst, search_str)

                case '0':
                    exit()

                case _:
                    print("invalid input")


        

        
    # book_count = load_books(books_lib_path, books_lst)
    # print(f"Total books loaded: {book_count}")
    
    




# o	Present the menu, get and evaluate user’s selection,
#  repeating until user chooses to quit:
# 	Get additional user inputs as needed
# 	Call appropriate functions to help perform the actions
#  for each menu option
# 	Display relevant context/status messages
# o	Call save_books() to save list of Books to file before
#  ending the program


if __name__ == "__main__":
    main()