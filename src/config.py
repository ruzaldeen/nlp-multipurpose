'''
config.py
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, seaborn as sns
import streamlit as st

class Config:

    hide_streamlit_style = '''
			<style>
            footer {visibility: hidden;}
            footer:after {
            content:'_____________________________Developed and Deployed by Ruzaldeen Zainal Abidin________________________________';
            visibility: visible;
            display: block;
            position: relative;
            }
            </style>
            
            '''