# Case Study 5: Library Catalog & Circulation Desk

#Task 1: Library Catalog
catalog = {
    101: {
        "title": "Cpp",
        "author": "Balagurudsamy"
    },
    102: {
        "title": "Java",
        "author": "Jack"
    },
    103: {
        "title": "Python Programming",
        "author": "Unknown"
    }
}

#Task 2: Available and Issued Books

available_books = {
    101,
    102,
    103
}

issued_books = set()

#Task 3: Issue Boook

def issueBook(book_id):

    if book_id in catalog:

        if book_id in available_books:

            available_books.remove(book_id)
            issued_books.add(book_id)

            print("Book issued successfully.")

        else:

            print("Book is already issued.")

    else:

        print("Book ID not found.")


# Task 4: Return Book
def return_book(book_id):

    if book_id in issued_books:

        issued_books.remove(book_id)
        available_books.add(book_id)

        print("Book returned successfully.")

    else:

        print("This book is not currently issued.")


# Menu

while True:

    print("\n===== LIBRARY MENU =====")
    print("1. Display Catalog")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")


    # Option 1: Display Catalog

    if choice == "1":

        print("\nLibrary Catalog:")

        for book_id, details in catalog.items():

            if book_id in available_books:
                status = "AVAILABLE"

            elif book_id in issued_books:
                status = "ISSUED"

            else:
                status = "UNKNOWN"

            print(
                book_id,
                "|",
                details["title"],
                "|",
                status
            )


    # Option 2: Issue Book

    elif choice == "2":

        book_id = int(input("Enter Book ID to issue: "))

        issueBook(book_id)


    # Option 3: Return Book

    elif choice == "3":

        book_id = int(input("Enter Book ID to return: "))

        return_book(book_id)


    # Option 4: Exit

    elif choice == "4":

        print("Exiting library system...")
        break


    # Invalid choice

    else:

        print("Invalid choice. Please try again.")


# Task 5: Library Dashboard

print("\n")
print("=" * 60)
print("          LIBRARY CATALOG STATUS DASHBOARD")
print("=" * 60)

print(
    f"{'ID':<7} | "
    f"{'Book Title':<23} | "
    f"{'Status':<10}"
)

print("-" * 60)


for book_id, details in catalog.items():

    if book_id in available_books:

        status = "AVAILABLE"

    else:

        status = "ISSUED"

    print(
        f"{book_id:<7} | "
        f"{details['title']:<23} | "
        f"{status:<10}"
    )


print("-" * 60)

total_books = len(catalog)
total_available = len(available_books)
total_issued = len(issued_books)

print(f"Total Catalog Books   : {total_books}")
print(f"Available Copies      : {total_available}")
print(f"Issued Copies         : {total_issued}")

print("=" * 60)
