from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self) -> str:
        pass


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, number_of_pages: int):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self) -> str:
        return (
            f"Title: {self.title}, Author: {self.author_or_director}, Year: {self.year}, Pages: {self.number_of_pages}"
        )


class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, year: int, issue_number: int):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def description(self) -> str:
        return f"Title: {self.title}, Author: {self.author_or_director}, Year: {self.year}, Issue: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, title: str, director: str, year: int, duration: int):
        super().__init__(title, director, year)
        self.duration = duration

    def description(self) -> str:
        return (
            f"Title: {self.title}, Director: {self.author_or_director}, "
            f"Year: {self.year}, Duration: {self.duration} minutes"
        )


book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
magazine = Magazine("National Geographic", "Various", 2021, 6)
dvd = DVD("Inception", "Christopher Nolan", 2010, 148)

print(book.description())
print(magazine.description())
print(dvd.description())
