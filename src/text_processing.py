#Author: Ruzaldeen Zainal Abidin 
'''
text_processing.py
'''

from nltk import text
from config import *

class TextProcessing(Config):

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data

    @classmethod
    def text_cleaning(cls, text_list):
        stop_words = set(stopwords.words('english'))
        byte_text = b' '.join(text_list)
        proc_text = str(byte_text).lower()
        proc_text = BeautifulSoup(proc_text, "lxml").text
        proc_text = re.sub(r'\([^)]*\)', '', proc_text)
        proc_text = re.sub('"','', proc_text)
        proc_text = " ".join([Config.contraction_mapping_english[x] if x in Config.contraction_mapping_english 
                            else x for x in proc_text.split(" ")])
        proc_text = re.sub(r"'s\b","",proc_text)
        proc_text = re.sub("[^a-zA-Z]", " ", proc_text)

        tokens = [word for word in proc_text.split() if not word in stop_words]
        long_word = []
        for i in tokens:
            if len(i) >= 3:
                long_word.append(i)
        
        return (" ".join(long_word)).strip()
