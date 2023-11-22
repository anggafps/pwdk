def initialize_library():
    # Create a dictionary for the library data
    return {
        'Python for Data Science For Dummies': {'Author': 'John Paul Mueller', 'Total Copies': 2, 'Available Copies': 0, 'Genre': 'Data Science', 'Publication Year': 2015},
        'Data Science for Business': {'Author': 'Foster Provost and Tom Fawcett', 'Total Copies': 7, 'Available Copies': 6, 'Genre': 'Data Science', 'Publication Year': 2013},
        'SQL Performance Explained': {'Author': 'Markus Winand', 'Total Copies': 3, 'Available Copies': 3, 'Genre': 'SQL', 'Publication Year': 2014},
        'Python Machine Learning': {'Author': 'Sebastian Raschka', 'Total Copies': 9, 'Available Copies': 9, 'Genre': 'Machine Learning', 'Publication Year': 2015},
        'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow': {'Author': 'Aurélien Géron', 'Total Copies': 4, 'Available Copies': 4, 'Genre': 'Machine Learning', 'Publication Year': 2019}
    }

def show_option_menu():
    print("Library Management System")
    print("1. Data Management System")
    print("2. Borrowing System")
    print("3. Exit")


def show_crud_menu():
    print("\nData Management System")
    print("1. Add a new book")
    print("2. Change data of a book")
    print("3. Delete a book")
    print("4. Search for a book")
    print("5. Show all books")
    print("0. Back to main menu")


def show_borrowing_menu():
    print("\nBorrowing System")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Show borrowed books")
    print("0. Back to main menu")


def add_book(library_data):
    print("\nAdd a New Book")
    title = input("Enter the title of the book: ")

    if title in library_data:
        return f"Book '{title}' already exists in the library."

    author = input("Enter the author of the book: ")
    total_copies = get_numeric_input("Enter the total number of copies: ")
    genre = input("Enter the genre of the book: ")
    publication_year = get_numeric_input("Enter the publication year of the book: ")

    library_data[title] = {
        "Author": author,
        "Total Copies": total_copies,
        "Available Copies": total_copies,
        "Genre": genre,
        "Publication Year": publication_year,
    }

    return f"Book '{title}' has been successfully added to the library."


def change_book_data(library_data):
    print("\nChange Data of a Book")
    print("Books in the Library:")
    for i, title in enumerate(library_data, start=1):
        print(f"{i}. {title}")

    option = get_numeric_input("Enter the number of the book you want to edit (0 to cancel): ")

    if 0 < option <= len(library_data):
        selected_book = list(library_data.keys())[option - 1]
        print(f"\nEditing data for '{selected_book}':")

        new_author = input("Enter the new author (press Enter to keep the current author): ")
        new_total_copies = get_numeric_input(
            "Enter the new total number of copies (press Enter to keep the current value): ")
        new_genre = input("Enter the new genre (press Enter to keep the current genre): ")
        new_publication_year = get_numeric_input(
            "Enter the new publication year (press Enter to keep the current year): ")

        if new_author:
            library_data[selected_book]['Author'] = new_author

        if new_total_copies is not None:
            library_data[selected_book]['Total Copies'] = new_total_copies
            library_data[selected_book]['Available Copies'] = new_total_copies

        if new_genre:
            library_data[selected_book]['Genre'] = new_genre

        if new_publication_year is not None:
            library_data[selected_book]['Publication Year'] = new_publication_year

        return f"Data for book '{selected_book}' has been successfully updated."
    elif option == 0:
        return "Data change operation canceled."
    else:
        return "Invalid option. Please enter a number within the range."


def delete_book(library_data):
    print("\nDelete a Book")
    print("Books in the Library:")
    for i, title in enumerate(library_data, start=1):
        print(f"{i}. {title}")

    option = get_numeric_input("Enter the number of the book you want to delete (0 to cancel): ")

    if 0 < option <= len(library_data):
        selected_book = list(library_data.keys())[option - 1]
        confirm = input(f"Are you sure you want to delete '{selected_book}'? (yes/no): ").lower()

        if confirm == "yes":
            del library_data[selected_book]
            return f"Book '{selected_book}' has been successfully deleted from the library."
        else:
            return "Deletion canceled."
    elif option == 0:
        return "Deletion operation canceled."
    else:
        return "Invalid option. Please enter a number within the range."


def search_data(library_data):
    search_term = input("Enter the title or author to search: ")
    search_results = []

    for title, book_data in library_data.items():
        if search_term.lower() in title.lower() or search_term.lower() in book_data['Author'].lower():
            search_results.append((title, book_data))

    if search_results:
        print("\nSearch Results:")
        for title, book_data in search_results:
            print(f"Title: {title}")
            print(f"Author: {book_data['Author']}")
            print(f"Total Copies: {book_data['Total Copies']}")
            print(f"Available Copies: {book_data['Available Copies']}")
            print(f"Genre: {book_data['Genre']}")
            print(f"Publication Year: {book_data['Publication Year']}")
            print("-" * 30)
    else:
        print("No matching books found.")

def show_all_books(library_data):
    print("\nAll Books in the Library:")
    for index, (title, book_data) in enumerate(library_data.items(), start=1):
        print(f"{index}. Title: {title}")
        print(f"   Author: {book_data['Author']}")
        print(f"   Total Copies: {book_data['Total Copies']}")
        print(f"   Available Copies: {book_data['Available Copies']}")
        print(f"   Genre: {book_data['Genre']}")
        print(f"   Publication Year: {book_data['Publication Year']}")
        print("-" * 30)


def borrow_book(library_data):
    print("\nBorrow a Book")
    print("Books in the Library:")
    for i, title in enumerate(library_data, start=1):
        print(f"{i}. {title}")

    option = get_numeric_input("Enter the number of the book you want to borrow (0 to cancel): ")

    if 0 < option <= len(library_data):
        selected_book = list(library_data.keys())[option - 1]
        available_copies = library_data[selected_book]["Available Copies"]

        if available_copies > 0:
            library_data[selected_book]["Available Copies"] -= 1
            return f"Book '{selected_book}' has been successfully borrowed."
        else:
            return "Sorry, the book is currently not available."
    elif option == 0:
        return "Borrowing operation canceled."
    else:
        return "Invalid option. Please enter a number within the range."


def return_book(library_data):
    print("\nReturn a Book")
    print("Books in the Library:")
    for i, title in enumerate(library_data, start=1):
        print(f"{i}. {title}")

    option = get_numeric_input("Enter the number of the book you want to return (0 to cancel): ")

    if 0 < option <= len(library_data):
        selected_book = list(library_data.keys())[option - 1]
        library_data[selected_book]["Available Copies"] += 1
        return f"Book '{selected_book}' has been successfully returned."
    elif option == 0:
        return "Return operation canceled."
    else:
        return "Invalid option. Please enter a number within the range."


def show_borrowed_books(library_data):
    borrowed_books = [(title, book_data) for title, book_data in library_data.items() if
                      book_data["Total Copies"] - book_data["Available Copies"] > 0]

    if borrowed_books:
        print("\nBorrowed Books:")
        for title, book_data in borrowed_books:
            print(f"Title: {title}")
            print(f"Author: {book_data['Author']}")
            print(f"Total Copies: {book_data['Total Copies']}")
            print(f"Available Copies: {book_data['Available Copies']}")
            print(f"Genre: {book_data['Genre']}")
            print(f"Publication Year: {book_data['Publication Year']}")
            print("-" * 30)
    else:
        print("No books have been borrowed.")


def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if not user_input:
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    library_data = initialize_library()

    while True:
        show_option_menu()
        option = get_numeric_input("Enter the number of the option: ")

        if option == 1:
            while True:
                show_crud_menu()
                crud_option = get_numeric_input("Enter the number of the option: ")

                if crud_option == 1:
                    print(add_book(library_data))
                elif crud_option == 2:
                    print(change_book_data(library_data))
                elif crud_option == 3:
                    print(delete_book(library_data))
                elif crud_option == 4:
                    search_data(library_data)
                elif crud_option == 5:
                    show_all_books(library_data)
                elif crud_option == 0:
                    break
                else:
                    print("Invalid option. Please enter a number within the range.")

        elif option == 2:
            while True:
                show_borrowing_menu()
                borrow_option = get_numeric_input("Enter the number of the option: ")

                if borrow_option == 1:
                    print(borrow_book(library_data))
                elif borrow_option == 2:
                    print(return_book(library_data))
                elif borrow_option == 3:
                    show_borrowed_books(library_data)
                elif borrow_option == 0:
                    break
                else:
                    print("Invalid option. Please enter a number within the range.")

        elif option == 3:
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number within the range.")


main()