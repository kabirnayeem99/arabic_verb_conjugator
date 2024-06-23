import argostranslate.package
import argostranslate.translate

from_code = "ar"
to_code = "en"

def download_and_install_translate():
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

def translate_pronouns_to_en(pronouns):
    arabic_to_english = {
        "أنا": "I",
        "أَنَا": "I",
        "نحن": "we",
        "نَحْنُ": "we",
        "أنت": "you",
        "أَنْتَ": "you",
        "أنتِ": "you",
        "أَنْتِ": "you",
        "أنتما": "you",
        "أَنْتُمَا": "you",
        "أنتما مؤ": "you",
        "أَنْتُمَا مُؤَ": "you",
        "أنتم": "you",
        "أَنْتُمْ": "you",
        "أنتن": "you",
        "أَنْتُنَّ": "you",
        "هو": "he",
        "هُوَ": "he",
        "هي": "she",
        "هِيَ": "she",
        "هما": "they",
        "هُمَا": "they",
        "هما مؤ": "they",
        "هُمَا مُؤَ": "they",
        "هم": "they",
        "هُمْ": "they",
        "هن": "they",
        "هُنَّ": "they"
    }
    
    translated_pronouns = list(map(lambda pronoun: arabic_to_english.get(pronoun, pronoun), pronouns))
    
    return translated_pronouns

def translate_pronoun_to_en(pronoun):
    arabic_to_english = {
        "أنا": "I",
        "أَنَا": "I",
        "نحن": "we",
        "نَحْنُ": "we",
        "أنت": "you",
        "أَنْتَ": "you",
        "أنتِ": "you",
        "أَنْتِ": "you",
        "أنتما": "you",
        "أَنْتُمَا": "you",
        "أنتما مؤ": "you",
        "أَنْتُمَا مُؤَ": "you",
        "أنتم": "you",
        "أَنْتُمْ": "you",
        "أنتن": "you",
        "أَنْتُنَّ": "you",
        "هو": "he",
        "هُوَ": "he",
        "هي": "she",
        "هِيَ": "she",
        "هما": "they",
        "هُمَا": "they",
        "هما مؤ": "they",
        "هُمَا مُؤَ": "they",
        "هم": "they",
        "هُمْ": "they",
        "هن": "they",
        "هُنَّ": "they"
    }
    
    return arabic_to_english.get(pronoun, pronoun)

def translate_to_en(ar_word):
    return ""
    translatedText = argostranslate.translate.translate(ar_word, from_code, to_code)
    return translatedText