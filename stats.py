def word_counter(text):
    words = text.split()
    return len(words)


def character_counter(text):
    char_counts = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1
    return char_counts


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

