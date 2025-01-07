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

def convert_to_list_dict(dict):
    dict_list = []
    for member in dict:
        if member.isalpha():
            dict_list.append({"char": member, "count": dict[member]})
    return dict_list

def sort_on(dict): #function takes a dictionary return the value of the "count" key to sort with the .sort() method
    return dict["count"]

def read_book_from_file(path):
    with open(path) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book = read_book_from_file(book_path)

    chars_counts_list = convert_to_list_dict(count_chars(book))
    chars_counts_list.sort(reverse=True, key=sort_on)

    print(f"[--- Begin report of {book_path} ---]")
    print(f"There are {count_words(book)} words in this text.")
    print()
    for dict in chars_counts_list:
        print(f"The '{dict["char"]} character was found {dict["count"]} times")
    print("[--- End report ---]")

main()