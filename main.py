def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def word_count(text):
    num_words = text.split()
    return num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"{len(num_words)} words found in the document")
main()
