import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count
from stats import get_book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book_text = get_book_text(path)

    word_count = get_word_count(book_text)
    char_count_dict = get_char_count(book_text)
    sorted_char_count = sort_char_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()