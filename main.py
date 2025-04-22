import sys
from stats import word_count, letter_count, sorted_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words_counted = word_count(book_text)
    final_count = len(words_counted)
    final_letter_count = letter_count(book_text)
    sorted_letter_count = sorted_count(final_letter_count)
    print_report(book_path, final_count, sorted_letter_count)

def print_report(book_path, final_count, sorted_letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {final_count} total words")
    print("--------- Character Count -------")
    for item in sorted_letter_count:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
       
    #print(f"{final_count} words found in the document")
    # for i in final_letter_count:
    #   print(f"'{i}': {final_letter_count[i]}")
main()

