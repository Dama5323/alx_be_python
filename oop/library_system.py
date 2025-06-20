class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        """Initialize book with title and author."""
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title, author, file_size):
        """
        Initialize ebook with title, author and file size.
        
        Args:
            title (str): Book title
            author (str): Book author
            file_size (int): File size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    def __init__(self, title, author, page_count):
        """
        Initialize print book with title, author and page count.
        
        Args:
            title (str): Book title
            author (str): Book author
            page_count (int): Number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library using composition to manage books."""
    def __init__(self):
        """Initialize library with empty book collection."""
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): Book instance to add
        """
        self.books.append(book)
    
    def list_books(self):
        """Print all books in the library."""
        for book in self.books:
            print(book)
    