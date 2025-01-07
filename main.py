def count_words(text):
    words = text.split()
    return len(words)

def read_book_from_file(path):
    with open(path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book = read_book_from_file(book_path)
    print(book)
    print(f"There are {count_words(book)} words.")

main()