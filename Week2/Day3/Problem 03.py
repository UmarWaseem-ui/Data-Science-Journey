# Library Books
# Create a DataFrame with:
    # Book Name
    # Author
    # Year Published

# Add at least 5 books of your choice and print the complete table.

import pandas as pd
LibraryBooks={
    "BookName" : ["To Kill a Mockingbird", "1984", "The Great Gatsby", "Pride and Prejudice", "The Hobbit"],
	"Authors" : ["Harper Lee", "George Orwell", "F. Scott Fitzgerald", "Jane Austen", "J.R.R. Tolkien"],
	"YearPublished" : [1960, 1949, 1925, 1813, 1937]
}

LB=pd.DataFrame(LibraryBooks)

print(LB)
		