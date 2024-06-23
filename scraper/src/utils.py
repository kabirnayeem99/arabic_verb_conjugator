import re

def is_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    return bool(arabic_pattern.search(text))

def get_person_number(pronoun):
    plural_third_person = ["they", "they (two)", "they (two - dual polite)"]
    singular_third_person = ["he", "she", "it"]
    plural_second_person = ["you (plural)", "you (female - plural)", "you (two)", "you (two - dual polite)"]
    singular_second_person = ["you (male)", "you (female)", "you"]
    singular_first_person = ["i"]
    plural_first_person = ["we"]

    only_pronoun = remove_parentheses_content(pronoun)
    
    if only_pronoun.lower() in singular_third_person:
        return "third", "singular"
    elif only_pronoun.lower() in plural_third_person:
        return "third", "plural"
    elif only_pronoun.lower() in singular_second_person:
        return "second", "singular"
    elif only_pronoun.lower() in singular_first_person:
        return "first", "singular"
    elif only_pronoun.lower() in plural_second_person:
        return "second", "plural"
    elif only_pronoun.lower() in plural_first_person:
        return "first", "plural"
    else:
        return "", ""

def remove_parentheses_content(s):
    return re.sub(r'\([^)]*\)', '', s).strip()

def remove_harakat(word):
    harakat_pattern = "[ًٌٍَُِّْ]"
    cleaned_word = re.sub(harakat_pattern, "", word)
    return cleaned_word

def remove_to(text):
    if text.startswith("to "):
        return text[3:].strip()
    return text.strip()

def has_only_one_word(text):
    words = text.split(" ")
    return len(words) == 1
