def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
from stats import word_count, num_char, sorting_keys, dictionary_list
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    def main():
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = word_count(book_text)
        characters = num_char(book_text)
        dict_list = dictionary_list(characters)
        dict_list.sort(reverse=True, key=sorting_keys)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {len(num_words)} total words")
        print("--------- Character Count -------")
        for items in dict_list:
            print(f"{items["char"]}: {items["num"]}")
main()
