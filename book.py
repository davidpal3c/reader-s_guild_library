

# from test_book import book_list

class Book:

    GENRE = { 0: "Romance",
                1: "Mystery",
                2: "Science Fiction",
                3: "Thriller",
                4: "Young Adult",
                5: "Children's Fiction",
                6: "Self-help",
                7: "Fantasy",
                8: "Historical Fiction",
                9: "Poetry"}

    def __init__(self, isbn, title, author, genre_id, availability):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre_id)
        self.__availability = bool(availability)


    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre_name(self):
        for key, val in Book.GENRE.items():
            if key == self.__genre:
                return val

    def str_to_bool(self):
        return self.__availability.lower() == "true"


    def get_availability(self):
        return "Available" if self.__availability else "Borrowed"

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre_id):
        self.__genre = genre_id
  

    def borrow_it(self):
        if self.__availability: 
            self.__availability = False
        else: 
            print(f"Book not available")


    def return_it(self):
        if not self.__availability:
            self.__availability = True
        else:
            print(f"Book ")


    def __str__(self):
        return "{:15s} {:26s} {:27s} {:<21} {:<20}".format(
            self.get_isbn(),
            self.get_title(),
            self.get_author(),
            self.get_genre_name(),
            self.get_availability()
        )  

# CLASS TEST
# genre1 = Book("978-0060513030", "Where the Sidewalk Ends", "Shel Silverstein", 9, False)
# print(genre1.get_genre_name())