

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
        
        # Checks if value passed as attribute is boolean and converts it if it isn't
        if isinstance(availability, bool):
            self.__availability = availability
        else:
            self.__availability = availability.lower() == "true"


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
            # else:
            #     return "Unknown Genre"

    # def str_to_bool(self):
    #     return self.__availability.lower() == "true"


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
            self.__availability = "True"
        # else:
        #     self.__availability = "False"


    # search method: includes search for title, author, and genre attributes" 
    def match_search(self, search_str):
        search_lower = search_str.lower()       
        
        if (search_lower in self.__isbn.lower() or
            search_lower in self.__title.lower() or
            search_lower in self.__author.lower()):
            return True
        
        for key, val in Book.GENRE.items():
            if search_lower in val.lower():
                if key == self.__genre:
                    return True
        
        return False


    def __str__(self):
        return "{:15s} {:26s} {:27s} {:<21} {:<20}".format(
            self.get_isbn(),
            self.get_title(),
            self.get_author(),
            self.get_genre_name(),
            self.get_availability()
        )  

# # CLASS TEST
# genre1 = Book("978-0060513030", "Where the Sidewalk Ends", "Shel Silverstein", 9, False)
# print(genre1.get_genre_name())