# Counts the number of words in the provided book and returns that number
def count_words(book_text):
    words = book_text.split()
    return len(words)

# Counts the number of each individual character, including spaces and symbols, and returns a dictionary of (character: count of character)
def count_characters(book_text):
    char_dict = {}

    for character in book_text:
        low_char = character.lower()
        if low_char not in char_dict:
            char_dict[low_char] = 1
        else:
            char_dict[low_char] += 1
    return char_dict

# Takes an imported dictionary and returns a new list, where each item on the list is a dictionary that represents each character with it's count
def sort_dict(dict):
    def sort_by(dict):
        return dict["count"]

    list_of_dict = []

    for key in dict:
        value = dict[key]
        new_dict = {"character": key, "count": value}
        list_of_dict.append(new_dict)
    
    list_of_dict.sort(reverse=True, key=sort_by)
    return list_of_dict
