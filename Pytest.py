import pytest

from Next_Queue_Position_And_Book_Search import get_next_queue_position,search_book_list

# 1. Normal condition
def test_next_queue_position():
    result = get_next_queue_position(3)
    assert result == 4


# 2. First reservation / empty queue
def test_first_reservation():
    result = get_next_queue_position(None)
    assert result == 1


# 3. Queue with one existing reservation
def test_next_position_after_one_reservation():
    result = get_next_queue_position(1)
    assert result == 2


# 4. Large queue position
def test_next_position_for_large_queue():
    result = get_next_queue_position(100)
    assert result == 101


# 5. Invalid string input
def test_string_input_raises_error():
    with pytest.raises(ValueError):
        get_next_queue_position("three")


# 6. Invalid decimal input
def test_decimal_input_raises_error():
    with pytest.raises(ValueError):
        get_next_queue_position(2.5)


# 7. Invalid zero position
def test_zero_position_raises_error():
    with pytest.raises(ValueError):
        get_next_queue_position(0)


# 8. Invalid negative position
def test_negative_position_raises_error():
    with pytest.raises(ValueError):
        get_next_queue_position(-1)


books = [
    {
        "title": "Atomic Habits",
        "author": "James Clear"
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho"
    },
    {
        "title": "Clean Code",
        "author": "Robert C. Martin"
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt"
    }
] # Sample book database


# 1. Search by exact title
def test_search_by_title():

    result = search_book_list(books, "Atomic Habits")

    assert len(result) == 1
    assert result[0]["title"] == "Atomic Habits"


# 2. Search by author
def test_search_by_author():

    result = search_book_list(books, "Paulo Coelho")

    assert result[0]["author"] == "Paulo Coelho"


# 3. Partial search
def test_search_by_partial_title():

    result = search_book_list(books, "Atomic")

    assert result[0]["title"] == "Atomic Habits"


# 4. Case-insensitive search
def test_search_is_case_insensitive():

    result = search_book_list(books, "aToMiC")

    assert result[0]["title"] == "Atomic Habits"


# 5. No matching book
def test_search_no_matching_book():

    result = search_book_list(books, "Harry Potter")

    assert result == "No matching book found"

# 6. No value is entered
def test_search_no_data():

    result = search_book_list(books,"")

    assert result == "Please enter a book name or author name"