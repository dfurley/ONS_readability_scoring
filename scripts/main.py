# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:12:20 2022

@author: furled
"""

# import libraries
import textstat as tx
import streamlit as st

st.title('ONS recruitment - readability scoring')

text = st.text_area(label = 'Text to analyse', value = 'Input text to analyse here', height = 300)

st.write('Reading ease: {:.2f}'.format(tx.flesch_reading_ease(text)))
st.write('Grade level: {:.2f}'.format(tx.flesch_kincaid_grade(text)))