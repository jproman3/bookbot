def word_count(book_text):
    count = book_text.split()
    return count

def letter_count(book_text):
    lower_book = book_text.lower()
    letter_count = {}
    for letter in lower_book:
        if letter in letter_count:
            letter_count[letter] += 1
        else: 
            letter_count[letter] = 1
    return letter_count

def sort_on(d):
    return d["num"]

def sorted_count(letter_count):
    descending_sort = []
    for i in letter_count:
        descending_sort.append({"char": i, "num": letter_count[i]})
    descending_sort.sort(reverse=True, key=sort_on)
    return descending_sort

