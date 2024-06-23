import libqutrub.conjugator
from src.extract_verbs_from_csv import extract_verbs_from_csv
from src.qutrub_api_service import call_qutrub_api, pretty_print_json
import sys
import time
from libqutrub import conjugator
from src.db import create_new_table, insert_conjugator_data
from src.english_verbs.conjugate import conjugate;
from src.translate_service import translate_to_en, download_and_install_translate
from src.corpus.corpus_verbs_scraper import extract_verbs_with_meaning

def main():
    print("╔════════════════════════════════════╗")
    print("║      Verb Conjugator Program       ║")
    print("╚════════════════════════════════════╝")
    csv_file = 'data/verblist.csv' 
    create_new_table()
    print(f"🔄 Loading verbs from CSV file...\n")
    download_and_install_translate()
    extracted_verbs, extracted_meanings, verb_meanings = extract_verbs_with_meaning()
    all_verbs = extracted_verbs
    # all_verbs = []
    # already_added = set()
    # [all_verbs.append(v) for v in extracted_verbs if v not in already_added and not already_added.add(v)]

    total_verbs = len(all_verbs)
    print(f"📘 Total Verbs Extracted: {total_verbs}\n")
    print(f"🔄 Loading verbs from API...\n")

    show_progress_bar(1, total_verbs)
    
    for idx, verb in enumerate(all_verbs, start=1):
        try:
            if (len(extracted_meanings)<idx):
                continue
            meaning = verb_meanings[verb]
            future_type =u"فتحة"
            table = conjugator.conjugate(verb,future_type,past=True, future=True, imperative=True, passive=True,  display_format="TABLE");
            insert_conjugator_data(verb, meaning, table) 
            show_progress_bar(idx, total_verbs)
        except IndexError:
            print("Index out of range")

    show_progress_bar(total_verbs, total_verbs)

def show_progress_bar(current_item, total_items, bar_length=50):
    progress = int(current_item / total_items * 100)
    progress_string = f"Progress: [{'=' * int(progress / (100 / bar_length))}{' ' * (bar_length - int(progress / (100 / bar_length)))}] {progress}%\nProcessing item {current_item} of {total_items}"
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write('\r')
    sys.stdout.write('\r')
    sys.stdout.write(progress_string)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
