from stats import get_num_words, get_char_count, get_sorted_list_of_dict
import sys

def get_book_text(file_path):
    file_string = ""
    
    with open(file_path) as f:
        file_string = f.read()

    return file_string

def get_book_path():
    args = sys.argv
    if (len(args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[1]

def main():
    book_path = get_book_path()
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_char_count(book_text)
    sorted_list_of_dicts = get_sorted_list_of_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list_of_dicts:
        if (dict["name"].isalpha()):
            print(f'{dict["name"]}: {dict["num"]}')

main()