Books = ['things fall apart', 'when love visits', 'baba segi and his wives', 'ogadinma', 'welcome to lagos', 'golibe', 'how to grow wings']
 
def view_Books():
    if Books:
        print('Books Avaliable:')
        for idx, book in enumerate(Books, start = 1):
            print(f"{idx} - {book}")
    
    else:
        print('No books are currently avaliable')

def borrow_Books():
    if not Books:
        print('no books are avaliable at the moment')
        return

    view_Books()
    try:
        choice = int(input('enter number of the book you want to borrow: '))
        if 1<= choice <= len(Books):
            Book = Books.pop(choice - 1)
            print(f'you have just borrowed "{Book}".')
        else:
            print('Not applicable! input a valid number')
    except ValueError:
        print('enter a valid number')

def return_Books():
    Books = input()

