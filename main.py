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



def print_books():
    pass

# (menu option 6, 1)
# •	Receives a book list
# •	Displays a book information heading, then iterates through the book list displaying each Book object on a separate line



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



def search_books():
    pass
# (menu option 1)
# •	Before calling this function, input search string from user
# •	Receives a book list and a search string
# •	Iterates through the list of books and checks if the search string 
# appears in isbn, title, author, or genre name. If any match is found, 
# the book is added to the search result list.
# •	Returns search result list
# •	After calling this function, call print_books() passing to it the 
# search result list






def print_menu():
    pass
# •	Receives menu heading (string) and menu options (dict)
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

            book = Book(isbn, title, author, genre, availability)

            books_lst.append(book)

            bCount += 1

        for book in books_lst:
            print(book)

            
        return bCount


# •	Receives an empty list and pathname to an existing CSV file
# •	Iterates over each line (i.e. book) in the file, parsing the attribute values into separate variables
# •	Creates Book objects from each set of attributes and adds them one-by-one onto the list
# •	Returns the number of books loaded




def main(): 

    print("Starting the system...")

    input_path = input("Enter book catalog filename: ")
    books_lib_path = os.path.join(os.getcwd(), input_path)
    
    if not os.path.exists(books_lib_path):
        print(f"{input_path} does not exists - Exiting.")
        return
    
    books_lst = []
    book_count = load_books(books_lib_path, books_lst)

    print(f"Total books loaded: {book_count}")
    print('Book catalog has been loaded')



# •	Entry point for the Library Management System
# •	Coordinates the overall processing:
# o	Set up a list of books
# o	Input pathname of CSV data file from user and call 
# load_books() to populate the list of books
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