def get_next_queue_position(last_position): # Function to find the next queue position when a person tries to make a reservation
    if last_position is None:
        return 1
    elif not isinstance(last_position, int): 
        raise ValueError("Queue position must be an integer.")
    elif last_position < 1:
        raise ValueError("Queue position must be greater than 0.")
    else:
        return last_position + 1 


def search_book_list(books, query): # Function for search the book using book or author name
    query = query.strip().lower()

    if not query: # condition for not entering any name
        return "Please enter a book name or author name"

    
    book_list=[ book for book in books if query in book["title"].lower() or query in book["author"].lower() ] # List comprehension for storing all the matching book results

    if len(book_list)==0:
        return "No matching book found"
    else: 
        return book_list