# use built in python function on python objects
class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'the book named {self.name} written by {self.author} has {self.pages} pages'
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object is deleted")
mybook = Book('Fifty','Green',200)
print(mybook)
print(len(mybook))

#delete an object
del mybook
