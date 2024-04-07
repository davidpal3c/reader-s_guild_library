


class Book:

    def __init__(self, isbn, title, author, genre, bool):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__availablitiy = bool


    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre_name(self):
        return self.__genre
    
    def get_availability(self):
        return self.__availablitiy


    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = int(genre)
  

    def borrow_it(self):
        return self
    
    def return_it(self):
        pass




    def __str__(self):
        return f"{self.get_isbn()}"