import csv

def extract_verbs_from_csv(csv_file):
    verbs = []
    meanings = []

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                verb = row[0].strip()
                meaning = row[1].strip()
                verbs.append(verb)
                meanings.append(meaning)

    return verbs, meanings

