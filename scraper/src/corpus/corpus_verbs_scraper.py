import requests
from bs4 import BeautifulSoup
import re
import time
from src.ui_utils import show_progress_bar
import requests_cache

base_url = 'https://corpus.quran.com/verbs.jsp'
requests_cache.install_cache('corpus_cache', expire_after=None)

def is_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    return bool(arabic_pattern.search(text))

def extract_verbs_with_meaning(): 

    print(f"🔄 Loading Quranic verbs from Quran Corpus...\n")

    show_progress_bar(1, 30)

    verb = []
    verbs_meanings = {}

    for page_number in range(1, 30):
        url = base_url+ "?" + "page=" + str(page_number)
        response = requests.get(url)
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
                first_column = columns[0].text.strip() 
                last_column = columns[-1].text.strip() 
                if first_column and last_column and is_arabic(first_column):
                    verb_word = first_column.strip()
                    verb.append(verb_word)
                    meaning_word = last_column.split(',')[0].strip()
                    verbs_meanings[verb_word] = meaning_word
    show_progress_bar(30, 30)

    total_verbs = len(verb)
    print(f"📘 Total Verbs Extracted: {total_verbs}\n")

    return verb, verbs_meanings