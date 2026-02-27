class Book:
    def __init__(self,title,author,isbn,status="avaliable"):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.status=status

    def issue(self):
        if self.is_available():
            self.status="issued"
            return True
    
    def return_book(self):
        self.status="avaliable"

    def to_dict(self):
        return{
            "title":self.title,
            "author":self.author,
            "isbn":self.isbn,
            "status":self.status


        }
    
    def __str__(self):
        return f"[{self.status.upper()}] {self.title} by {self.author} (ISBN: {self.isbn})"