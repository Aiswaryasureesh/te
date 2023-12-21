class Publisher:
    def __init__(self,n):
        self.name=n
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        print("Title:\t",self.title)
        print("Author
