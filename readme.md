# Reader's Guild Library Management System

A simple library management system implemented in Python. This application allows users to search for books, borrow and return books, add and remove books from the catalog, and print the catalog.

## Features

- **Search Books**: Search for books by ISBN, title, author, or genre.
- **Borrow Book**: Borrow a book from the catalog.
- **Return Book**: Return a borrowed book.
- **Add Book**: Add a new book to the catalog (Librarian only).
- **Remove Book**: Remove a book from the catalog (Librarian only).
- **Print Catalog**: Print the list of all books in the catalog (Librarian only).

## Dependencies

- Python 3.x

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system


2. **Run the program:**

    ```bash

    python main.py


3. **How to Use**

    Start the system:
    When you run the program, you will be prompted to enter the book catalog filename. Ensure that books.csv (or your catalog file) is in the same directory as main.py.

    Main Menu Options:
        1. Search for books: Enter a search term to find matching books.
        2. Borrow a book: Enter the ISBN of the book you want to borrow.
        3. Return a book: Enter the ISBN of the book you want to return.
        0. Exit the system: Save the catalog and exit the program.

    Librarian Menu Options:
    Enter the admin password (set line 16) to access the librarian menu.
        4. Add a book: Enter the details of the new book.
        5. Remove a book: Enter the ISBN of the book you want to remove.
        6. Print catalog: Print the entire catalog of books.

Project Structure

    book.py: Contains the Book class, which defines the book object and its methods.
    main.py: The main program file that handles user interaction and program flow.
    books.csv: A sample CSV file containing the book catalog.

Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or enhancements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
