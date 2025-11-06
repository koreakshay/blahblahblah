import sys
from stats import get_num_words, get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# def get_num_words(text):
#     return len(text.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_counts = sorted(char_count.items(), reverse=True, key=lambda x: x[1])
    for char,count in sorted_counts:
        if char.isalpha():
            print(f'{char}: {count}')

if __name__ == "__main__":
    main()