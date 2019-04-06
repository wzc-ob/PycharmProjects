class Book:
    def __init__(self,name="Python 从入门到精通"):
        self.name = name
    def __add__(self, obj):
        return self.name + 'add'+obj.name
    def __len__(self):
        return len(self.name)
if __name__ == '__main__':
    booka = Book()
    bookb =Book('Java 从入门到精通')
    print("len(booka):",len(booka))
    print("len(bookb):",len(bookb))
    print(booka +bookb)