import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import requests_cache

base_url = 'https://corpus.quran.com/verbs.jsp'
requests_cache.install_cache('corpus_cache', expire_after=None)

def is_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    return bool(arabic_pattern.search(text))

def extract_verbs_with_meaning(): 
    show_progress_bar(1, 30)
    verb = []
    meaning = []
    verbs_meanings = {}
    for page_number in range(1, 30):
        url = base_url+ "?" + "page=" + str(page_number)
        response = requests.get(url)
        time.sleep(0.12)
        show_progress_bar(page_number, 30)
        if response.status_code == 200:
            html_content = response.text
        else:
            print("Error to load page {page_number}. URL: ${url}")
            continue
        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if columns:
                first_column = columns[0].text.strip()  # First column text
                last_column = columns[-1].text.strip()  # Last column text
                if first_column and last_column and is_arabic(first_column):
                    verb_word = first_column.strip()
                    verb.append(verb_word)
                    meaning_word = last_column.split(',')[0].strip()
                    meaning.append(meaning_word)
                    verbs_meanings[verb_word] = meaning_word
    show_progress_bar(30, 30)
    return verb, meaning, verbs_meanings


def show_progress_bar(current_item, total_items, bar_length=50):
    progress = int(current_item / total_items * 100)
    progress_string = f"Progress: [{'=' * int(progress / (100 / bar_length))}{' ' * (bar_length - int(progress / (100 / bar_length)))}] {progress}%\nProcessing item {current_item} of {total_items}"
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write('\r')
    sys.stdout.write('\r')
    sys.stdout.write(progress_string)
    sys.stdout.flush()
