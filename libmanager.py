# Initialize empt lists,  set, and dictionary
books_list = []
authors_set = set()
books_dict = {}

# Add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data Strurcture and Algorithms")
authors_set.add("John Doe")
books_dict["Data Strurcture and Algorithms"] = "John Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

# Search for a book 
search_title = input("Enter the tittle of the books to search: ")
if search_title in books_list
  print(f"Books found Author: {books_dict[search_title]}")
else:
  print("Books not found")
