import sqlite3
from src.translate_service import translate_to_en, translate_pronoun_to_en
from src.english_verbs import conjugate
import re

def create_new_table():
    conn = sqlite3.connect('generated/verbs.db')

    cursor = conn.cursor()

    drop_table_sql = """
    DROP TABLE IF EXISTS VerbConjugations
    """
    cursor.execute(drop_table_sql)

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS VerbConjugations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            word_meaning TEXT,
            pronoun TEXT,
            pronoun_meaning TEXT,
            past_known TEXT,
            past_known_meaning TEXT,
            present_known TEXT,
            present_known_meaning TEXT,
            present_subjunctive TEXT,
            present_subjunctive_meaning TEXT,
            present_construct TEXT,
            present_construct_meaning TEXT,
            present_confirmed_heavy TEXT,
            present_confirmed_heavy_meaning TEXT,
            imperative TEXT,
            imperative_meaning TEXT,
            confirmed_imperative TEXT,
            confirmed_imperative_meaning TEXT,
            past_unknown TEXT,
            past_unknown_meaning TEXT,
            present_unknown TEXT,
            present_unknown_meaning TEXT,
            present_unknown_subjunctive TEXT,
            present_unknown_subjunctive_meaning TEXT,
            present_unknown_construct TEXT,
            present_unknown_construct_meaning TEXT,
            present_confirmed_heavy_unknown TEXT,
            present_confirmed_heavy_unknown_meaning TEXT
    )
    """
    cursor.execute(create_table_sql)

    drop_index_word_sql = """
    DROP INDEX IF EXISTS idx_word;
    """
    cursor.execute(drop_index_word_sql)

    create_index_word_sql = """
    CREATE INDEX idx_word ON VerbConjugations (word);
    """
    cursor.execute(create_index_word_sql)

    conn.commit()


def insert_conjugator_data(word, word_meaning, data):
    if not bool(data):
        return
    conn = sqlite3.connect('generated/verbs.db')
    insert_sql = """
    INSERT INTO VerbConjugations (
            word,
            word_meaning,
            pronoun, 
            pronoun_meaning, 
            past_known, 
            past_known_meaning,
            present_known, 
            present_known_meaning, 
            present_subjunctive, 
            present_subjunctive_meaning, 
            present_construct, 
            present_construct_meaning, 
            present_confirmed_heavy, 
            present_confirmed_heavy_meaning, 
            imperative, 
            imperative_meaning, 
            confirmed_imperative, 
            confirmed_imperative_meaning, 
            past_unknown, 
            past_unknown_meaning, 
            present_unknown, 
            present_unknown_meaning, 
            present_unknown_subjunctive, 
            present_unknown_subjunctive_meaning, 
            present_unknown_construct, 
            present_unknown_construct_meaning, 
            present_confirmed_heavy_unknown,
            present_confirmed_heavy_unknown_meaning
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """ 

    cursor = conn.cursor()
    third_person_male_past_known = data[9]
    if third_person_male_past_known is None:
        return
    word = remove_harakat(word)
    if word.strip() == "":
        return

    for key, values in data.items():
        if (key==0):
            continue

        pronoun = values.get(0, "")                            # pronoun
        if pronoun:
            pronoun_meaning = translate_pronoun_to_en(pronoun)   # pronoun_meaning
        else: 
            pronoun_meaning = ""

        past_known = values.get(1, "")                         # past_known
        if past_known:
            conj_verb = conjugate_english_verb(word_meaning, pronoun=pronoun_meaning, tense="past")
            if conj_verb:
                past_known_meaning = pronoun_meaning + " " + conj_verb 
            else:
                past_known_meaning = ""
        else:
            past_known_meaning = ""

        present_known = values.get(2, "")                      # present_known
        if present_known:
            conj_verb = conjugate_english_verb(word_meaning, pronoun=pronoun_meaning, tense="present")
            if conj_verb:
                present_known_meaning = pronoun_meaning + " " + conj_verb
            else:
                present_known_meaning = ""
        else:
            present_known_meaning = "" 

        present_subjunctive = values.get(3, "")                # present_subjunctive
        present_subjunctive_meaning = translate_to_en(values.get(3, "")) # present_subjunctive_meaning
        present_construct = values.get(4, "")                  # present_construct
        present_construct_meaning = translate_to_en(values.get(4, "")) # present_construct_meaning
        present_confirmed_heavy = values.get(5, "")            # present_confirmed_heavy
        present_confirmed_heavy_meaning = translate_to_en(values.get(5, "")) # present_confirmed_heavy_meaning
        imperative = values.get(6, "")                         # imperative
        if imperative:
            conj_verb =remove_to(word_meaning)
            imperative_meaning =  conj_verb.replace("not ", "Don't ") + "!" # imperative_meaning
        else:
            imperative_meaning = ""
        confirmed_imperative = values.get(7, "")               # confirmed_imperative
        confirmed_imperative_meaning = translate_to_en(values.get(7, "")) # confirmed_imperative_meaning
        past_unknown = values.get(8, "")                       # past_unknown
        past_unknown_meaning = translate_to_en(values.get(8, "")) # past_unknown_meaning
        present_unknown = values.get(9, "")                    # present_unknown
        present_unknown_meaning = translate_to_en(values.get(9, "")) # present_unknown_meaning
        present_unknown_subjunctive = values.get(10, "")       # present_unknown_subjunctive
        present_unknown_subjunctive_meaning = translate_to_en(values.get(10, "")) # present_unknown_subjunctive_meaning
        present_unknown_construct = values.get(11, "")         # present_unknown_construct
        present_unknown_construct_meaning = translate_to_en(values.get(11, "")) # present_unknown_construct_meaning
        present_confirmed_heavy_unknown = values.get(12, "")   # present_confirmed_heavy_unknown
        present_confirmed_heavy_unknown_meaning = translate_to_en(values.get(12, "")) # present_confirmed_heavy_unknown_meaning
        params = (
            word,
            word_meaning,
            pronoun,
            pronoun_meaning,
            past_known,
            past_known_meaning,
            present_known,
            present_known_meaning,
            present_subjunctive,
            present_subjunctive_meaning,
            present_construct,
            present_construct_meaning,
            present_confirmed_heavy,
            present_confirmed_heavy_meaning,
            imperative,
            imperative_meaning,
            confirmed_imperative,
            confirmed_imperative_meaning,
            past_unknown,
            past_unknown_meaning,
            present_unknown,
            present_unknown_meaning,
            present_unknown_subjunctive,
            present_unknown_subjunctive_meaning,
            present_unknown_construct,
            present_unknown_construct_meaning,
            present_confirmed_heavy_unknown,
            present_confirmed_heavy_unknown_meaning
        )
        cursor.execute(insert_sql, params)

    conn.commit()

    cursor.close()
    conn.close()


def conjugate_english_verb(verb_phrase, pronoun = "he",tense = "present"):
    try: 
        person, number = get_person_number(pronoun=pronoun)
        verb_phrase = remove_to(verb_phrase)
        words = verb_phrase.split()
        verb = words[0].strip()

        if person and number:
            verb = conjugate.conjugate(verb, person=person,number=number,tense=tense)
            if verb is None: 
                return ""
            else:
                return verb + " " + " ".join(words[1:])
        
        irregular_verbs = {
            "have": "has",
            "do": "does",
            "be": "is"
        }
        
        if verb in irregular_verbs:
            return irregular_verbs[verb] + " " + " ".join(words[1:])
        
        if verb.endswith("s") or verb.endswith("sh") or verb.endswith("ch") or verb.endswith("x") or verb.endswith("z"):
            return verb + "es" + " " + " ".join(words[1:])
        elif verb.endswith("y") and verb[-2] not in "aeiou":
            return verb[:-1] + "ies" + " " + " ".join(words[1:])
        elif verb.endswith("o") and verb[-2] not in "aeiou":
            return verb + "es" + " " + " ".join(words[1:])
        else:
            return verb + "s" + " " + " ".join(words[1:])
    except:
        return ""

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
