from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        super().__init__(title, author)

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")


# Write MyBook class

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
