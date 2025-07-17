def get_num_words(string):
    return len(string.split())

def get_char_count(string):
    char_dict = {}

    for char in string:
        lowercase_char = char.lower()
        if (lowercase_char in char_dict):
            char_dict[lowercase_char] += 1
        else:
            char_dict[lowercase_char] = 1
    
    return char_dict

def get_list_from_dict(dict):
    list = []
    for key in dict:
        list.append({"name": key, "num": dict[key]})
    
    return list

def sort_on(items):
    return items["num"]
        
def get_sorted_list_of_dict(dict):
    list_of_dicts = get_list_from_dict(dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts