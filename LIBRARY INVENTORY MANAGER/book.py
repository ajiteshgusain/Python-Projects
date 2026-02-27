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
        return False
    
    def return_book(self):
        self.status="available"

    def is_avaliable(self):
# boolean expression. This means the computer evaluates it and immediately turns it into either True or False.        
#         return self.status=="available"
        
        if self.status=="available":
            return True
        else:
            return False
    

    def to_dict(self):
        return{
            "title":self.title,
            "author":self.author,
            "isbn":self.isbn,
            "status":self.status


        }
    
    def __str__(self):
        return f"[{self.status.upper()}] {self.title} by {self.author} (ISBN: {self.isbn})"