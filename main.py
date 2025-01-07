def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def read_book_from_file(path):
    with open(path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book = read_book_from_file(book_path)
    #print(book)
    print(f"There are {count_words(book)} words.")
    print(f"CHARS: {count_chars(book)}")

main()