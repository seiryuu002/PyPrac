# Magic  methods  or  dunder methods
# these are the special methods used 
# when when we want to perform python 
# inbuilt methods on our class object

class Book():
    def __init__(self, author, title, pages):
        self.author = author    
        self.title = title
        self.pages = pages
    
    def __str__(self):                         
        return f"{self.title} by {self.author}"
    def __len__(self):
        return int(self.pages)
    def __del__(self):
        print("book has been deleted")
mybook = Book('jose', 'python', '250')                          
print(mybook)        # normally print() would give error but here it calls function __str__()
print(len(mybook))   # normally len() would give error but here it calls function __len__()
del mybook           # this keyword 'del'deletes object and also calls function __del__()

