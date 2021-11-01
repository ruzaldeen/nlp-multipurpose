# Author: Ruzaldeen Zainal Abidin 
'''
text_processing.py
'''

from nltk import text
from config import *
from read_data import ReadData

class TextProcessing(ReadData):

    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return self.data

    def text_cleaning(self, input_type):
        '''
        Cleans the text from stopwords, contraction and other non-important elements.

        Args
        ----
        input_type : bool
            The method used to feed data. Uploaded file equals to True and direct string equals to False

        Returns
        -------
        proc_string : str
            The cleaned string
        '''
        stop_words = set(stopwords.words('english'))

        if input_type:
            byte_text = b' '.join(self.data)
            proc_text = str(byte_text).lower()
        else:
            proc_text = self.data.lower()

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
        
        proc_string = (" ".join(long_word)).strip()
        return proc_string

    
