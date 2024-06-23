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
        "أنت": "you (male)",
        "أَنْتَ": "you (male)",
        "أنتِ": "you (female)",
        "أَنْتِ": "you (female)",
        "أنتما": "you two",
        "أَنْتُمَا": "you two",
        "أنتما مؤ": "you two (dual polite)",
        "أَنْتُمَا مُؤَ": "you two (dual polite)",
        "أنتم": "you (plural)",
        "أَنْتُمْ": "you (plural)",
        "أنتن": "you (female plural)",
        "أَنْتُنَّ": "you (female plural)",
        "هو": "he",
        "هُوَ": "he",
        "هي": "she",
        "هِيَ": "she",
        "هما": "they two",
        "هُمَا": "they two",
        "هما مؤ": "they two (dual polite)",
        "هُمَا مُؤَ": "they two (dual polite)",
        "هم": "they (male)",
        "هُمْ": "they (male)",
        "هن": "they (female)",
        "هُنَّ": "they (female)"
    }
    
    translated_pronouns = list(map(lambda pronoun: arabic_to_english.get(pronoun, pronoun), pronouns))
    
    return translated_pronouns

def translate_pronoun_to_en(pronoun):
    arabic_to_english = {
        "أنا": "I",
        "أَنَا": "I",
        "نحن": "we",
        "نَحْنُ": "we",
        "أنت": "you (male)",
        "أَنْتَ": "you (male)",
        "أنتِ": "you (female)",
        "أَنْتِ": "you (female)",
        "أنتما": "you two",
        "أَنْتُمَا": "you two",
        "أنتما مؤ": "you two (dual polite)",
        "أَنْتُمَا مُؤَ": "you two (dual polite)",
        "أنتم": "you (plural)",
        "أَنْتُمْ": "you (plural)",
        "أنتن": "you (female plural)",
        "أَنْتُنَّ": "you (female plural)",
        "هو": "he",
        "هُوَ": "he",
        "هي": "she",
        "هِيَ": "she",
        "هما": "they two",
        "هُمَا": "they two",
        "هما مؤ": "they two (dual polite)",
        "هُمَا مُؤَ": "they two (dual polite)",
        "هم": "they (male)",
        "هُمْ": "they (male)",
        "هن": "they (female)",
        "هُنَّ": "they (female)"
    }
    
    return arabic_to_english.get(pronoun, pronoun)

def translate_to_en(ar_word):
    return ""
    translatedText = argostranslate.translate.translate(ar_word, from_code, to_code)
    return translatedText