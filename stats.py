def get_wordcount(book_text):
    word_count = book_text.split()
    return len(word_count)  

def get_characters(book_text):
    book_text = book_text.lower()
    letters = {}
    for i in book_text:
        letters[i] = letters.get(i, 0) + 1
    return letters

def sort_on(d):
    return d["num"]

def report(char_counts):
    result = []
    for ch, count in char_counts.items():
        if ch.isalpha():
            result.append({"char": ch, "num": count})

    result.sort(reverse=True, key=sort_on)
    return result
