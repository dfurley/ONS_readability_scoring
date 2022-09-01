# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:12:20 2022

@author: furled

Script to run streamlit app for FK score analysis
"""

# import libraries
import textstat as tx
import streamlit as st

# import local modules
import text_analysis_functions

st.title("ONS recruitment - readability scoring")

st.subheader("What is readability?")

st.markdown("Readability refers to how easy a piece of text is to read. There are various different methods for assessing text readability. This tool focuses on two different readability tests, the Flesch reading ease score and the Flesch Kincaid reading grade level.")

st.markdown("Further reading about these two readability tests is avaliable <a href='https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests'>here.</a>", unsafe_allow_html=True)

st.subheader("How to use this app.")

st.markdown("Simply copy and paste the text you want to analyse (e.g. a job advert) into the text box below and press the 'Analyse' button. This will output both a Flesch readability score and a Flesch-Kincaid reading grade level, and compare these to standard UK school reading levels.")

text = st.text_area(label = 'Text to analyse', value = 'Input text to analyse here', height = 300)

analyse_button = st.button('Analyse')

reading_ease = tx.flesch_reading_ease(text)
grade_level = tx.flesch_kincaid_grade(text)

reading_ease_descriptive = text_analysis_functions.convert_score_to_descriptive(reading_ease)
grade_descriptive = text_analysis_functions.convert_grade_to_uk_education_level(grade_level)


if analyse_button:
    st.write('Reading ease: {:.2f}. {}'.format(reading_ease, reading_ease_descriptive))
    st.write('Grade level: {:.2f}. Equivalent to UK {} reading level.'.format(grade_level, grade_descriptive))