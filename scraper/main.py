from src.qutrub_service import get_verb_conjugator_tables
from src.db import create_new_table, insert_conjugator_data
from src.corpus.corpus_verbs_scraper import extract_verbs_with_meaning
from src.ui_utils import show_progress_bar, show_program_title

def main():

    show_program_title()

    create_new_table()

    all_verbs, verb_meanings = extract_verbs_with_meaning()

    total_verbs = len(all_verbs)
    show_progress_bar(1, total_verbs)

    all_conj_tables_dict = get_verb_conjugator_tables(all_verbs)
    
    for idx, verb in enumerate(all_verbs, start=1):
        try:
            meaning = verb_meanings[verb]
            table = all_conj_tables_dict[verb]
            insert_conjugator_data(verb, meaning, table) 
            show_progress_bar(idx, total_verbs)
        except IndexError:
            print("Index out of range")

    show_progress_bar(total_verbs, total_verbs)


if __name__ == "__main__":
    main()
