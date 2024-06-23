
from libqutrub import conjugator

def get_verb_conjugator_tables(verbs):
    tables ={}
    for verb in verbs:
        table =get_verb_conjugator_table(verb)
        tables[verb] = table
    return tables

def get_verb_conjugator_table(verb):
    future_type =u"فتحة"
    table = conjugator.conjugate(verb,future_type,past=True, future=True, imperative=True, passive=True,  display_format="TABLE");
    return table
           