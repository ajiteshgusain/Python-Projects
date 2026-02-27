class library_inventory:
    def __init__(self):
        #intializing an empty list to store book objects
        self.books=[]


    def add_book(self,book):
            """to add books to the inventory"""
            self.books.append(book)

    def search_bytitle(self,title):
         """Returns a list of books that match the search title."""
         return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_isbn(self,isbn):
         """returns a single book matching the unique ISBN"""

         for book in self.books:
              if book.isbn==isbn:
                   return book
         
         return  None

def dispaly_all(self):
     """print all the books in the inventory"""
     if not self.books:
          print("the library is currenty empty.")

     else:
          for book in self.books:
               print(book)
 

        
