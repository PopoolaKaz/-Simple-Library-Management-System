books = ['Things fall apart', 'When love visits', 'The secret lives of Baba segi wives', 'Ogadinma', 'Welcome to lagos', 'Golibe', 'How to grow wings']

def view_books():
    if books:
        print('\nThese are the books I currently have;\n')
        for idx, book in enumerate (books, start = 1):
            print(f'{idx}. {book}')

    else: 
        print('No books are currently avalaible')

def borrow_book():
    if not books:
        print('\nThere are no books avaliable to borrow at the moment.')
        return
    
    view_books()
    if books:
        book_name = input('\nEnter the name of the book you want to borrow: ')
        if book_name in books:
            books.remove(book_name)
            print (f'\nYou have borrowed "{book_name}".')
        else:
            print ('The book is not avaliable')


def return_book():
    book_name = input('\nEnter the name of the book you want to return: ')
    
    if book_name in books:
        print(f'\n"{book_name}" is already in the library!')
    else:
        books.append(book_name)
        print(f'Thank you! You have returned "{book_name}"')

def myLibrary():
    while True:
        print("\nWhat do you want to do at my Library?\n")
        print("1. View the books I have available")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Leave the library")

        choice = input('\nEnter your choice (pick any number from 1-4): ')

        if choice =='1':
            view_books()

        elif choice == '2':
            borrow_book()

        elif choice == '3':
            return_book()

        elif choice == '4':
            print('\nThank you for visiting my library')
            break
        
        else:
            print('Not Applicable! Please try again')

myLibrary()