def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    words = text.lower().split()
    for word in words:
        for char in word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def read_book_from_file(path):
    with open(path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book = read_book_from_file(book_path)
    #print(book)
    print(f"There are {count_words(book)} words.")
    print(f"TEST: {count_chars(book)}")

main()