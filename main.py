from stats import get_wordcount

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = get_wordcount(book_text)
    print(f"{num_words} words found in the document")



main()
