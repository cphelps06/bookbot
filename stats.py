def word_count(text):
    num_words = text.split()
    return num_words

def num_char(text):
    char = {}
    lower_text = text.lower()
    for n in lower_text:
        if n in char:
            char[n] += 1
        else:
            char[n] = 1
    return(char)

def dictionary_list(dictionary):
   
    result = []
    for item in dictionary:
        new_dict = {}
        if item.isalpha():
            new_dict["char"]=item
            new_dict["num"] = dictionary[item]
            result.append(new_dict)
    return(result)

def sorting_keys(result):
    return result["num"]

