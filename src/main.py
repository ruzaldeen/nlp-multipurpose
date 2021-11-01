# Author: Ruzaldeen Zainal Abidin
'''
main.py
'''

from config import *
from read_data import ReadData
from text_processing import TextProcessing

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'>Multipurpose Natural Language Processing App</h1>", 
            unsafe_allow_html=True)
st.markdown(Config.hide_streamlit_style, unsafe_allow_html=True)

data_choice = st.radio("Select your preferred way of data input", ('Upload a file', 'Direct text input'))

if data_choice == 'Upload a file':
    uploaded_file = st.sidebar.file_uploader("Upload your file:", type=['txt'])
    read_obj = ReadData(uploaded_file)
    data = read_obj.read_file_txt()
    input_type = True

else:
    data = st.text_input('Input your text here:')
    input_type = False

if data is not None:
    model_option = st.selectbox("Please choose your intended model:", ["Text Summarization"])
    process_obj = TextProcessing(data)
    cleaned_data = process_obj.text_cleaning(input_type)

    

    
    
    