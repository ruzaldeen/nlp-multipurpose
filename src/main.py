# Author: Ruzaldeen Zainal Abidin
'''
main.py
'''

from config import *
from text_processing import TextProcessing

st.set_page_config(layout="wide")

def read_file():
    '''
    Reads the txt file input

    Args:
    open (boolean): True opens the file, False closes the file

    Returns:
    The whole text from the file
    '''
    uploaded_file = st.sidebar.file_uploader("Upload your file:", type=['txt'])
    
    # try:
    text_line = []
    if uploaded_file:
        for line in uploaded_file:
            text_line.append(line)
    
    if len(text_line) > 0:
        return text_line
    else:
        return None


    # except UnboundLocalError:
    #     pass


st.markdown("<h1 style='text-align: center; color: black;'>Multipurpose Natural Language Processing App</h1>", 
            unsafe_allow_html=True)
st.markdown(Config.hide_streamlit_style, unsafe_allow_html=True)

data = read_file()

if data is not None:
    model_option = st.selectbox("Please choose your intended model:", ["Text Summarization"])
    cleaned_data=TextProcessing.text_cleaning(data)
    
    