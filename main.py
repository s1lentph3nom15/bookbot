from stats import get_wordcount
from stats import get_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = get_wordcount(book_text)
    num_characters = get_characters(book_text)
    print(f"{num_words} words found in the document")
    print(num_characters)



main()
