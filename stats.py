def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    text = text.lower()
    chars_dict = {}
    for char in text:
        if char in chars_dict:
            chars_dict[char] = chars_dict[char] + 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_char_count(chars_dict):
    def sort_on(items):
        return items["num"]

    sorted_chars_dict_list = []
    for item in chars_dict:
        sorted_chars_dict_list.append({"char": item, "num": chars_dict[item]})

    sorted_chars_dict_list.sort(reverse=True, key=sort_on)
    return(sorted_chars_dict_list)