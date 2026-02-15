from stats import get_wordcount
from stats import get_characters
import sys
from stats import sort_on
from stats import report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 main.py <path_to_book>")

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    num_words = get_wordcount(book_text)
    char_counts = get_characters(book_text)
    final_report = report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in final_report:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

main()



