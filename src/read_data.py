# Author: Ruzaldeen Bin Zainal Abidin
'''
read_data.py
'''

from config import *

class ReadData(Config):
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data

    def read_file_txt(self):
        '''
        Reads the txt file input

        Returns:
        -------
        text_line : list
            The whole text from the file in a list
        '''
        
        # try:
        text_line = []
        if self.data:
            for line in self.data:
                text_line.append(line)
        
        if len(text_line) > 0:
            return text_line
        else:
            return None

