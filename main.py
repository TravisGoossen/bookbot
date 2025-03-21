from stats import count_words, count_characters , sort_dict
import sys

#Retrieves the text of any provided book
def get_book_path(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    #check if the CLI program is ran properly
    #if not, exit the program
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #set all variables to use cleanly
    book_path = sys.argv[1]
    book_to_analyze = get_book_path(book_path)
    word_count = count_words(book_to_analyze)
    char_count = count_characters(book_to_analyze)

    #The visual part of this program
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")   
    sorted_list = sort_dict(char_count)
    for i in range(len(sorted_list)):
        if sorted_list[i]["character"].isalpha():
            print(f"{sorted_list[i]["character"]}: {sorted_list[i]["count"]}")
    print("============= END ===============")

main()