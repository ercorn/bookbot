def count_words(book):
    words = book.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        print(file_contents)
        print(f"There are {count_words(file_contents)} words.")

main()