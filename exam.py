import mysql.connector

# Establish connection to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2019",
        database="library_db"
    )

# Add a new book to the database
def add_book(title, author, isbn):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, isbn))
    db.commit()
    print("Book added successfully.")
    cursor.close()
    db.close()

# Search for books by title
def search_books_by_title(search_term):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, ("%" + search_term + "%",))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
    else:
        print("No books found with that title.")
    cursor.close()
    db.close()

# List all books
def list_all_books():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}")
    cursor.close()
    db.close()

# Delete a book by ID
def delete_book(book_id):
    db = connect_db()
    cursor = db.cursor()
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    db.commit()
    if cursor.rowcount:
        print("Book deleted successfully.")
    else:
        print("No book found with that ID.")
    cursor.close()
    db.close()

# Example usage
if __name__ == "__main__":
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book by Title")
        print("3. List All Books")
        print("4. Delete Book by ID")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            add_book(title, author, isbn)
        elif choice == '2':
            search_term = input("Enter title to search: ")
            search_books_by_title(search_term)
        elif choice == '3':
            list_all_books()
        elif choice == '4':
            book_id = input("Enter Book ID to delete: ")
            delete_book(book_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

