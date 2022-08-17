# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:12:20 2022

@author: furled

Script to run streamlit app for FK score analysis
"""

# import libraries
import textstat as tx
import streamlit as st

def convert_grade_to_uk_education_level(grade):
    """
    Function to convert US grade level to UK education level.
    Takes one argument, 'grade'. This should be a float returned by the
    textstat 'flesch_kincaid_grade' function.

    Parameters
    ----------
    grade : float
        Float returned by the textstat 'flesch_kincaid_grade' function.

    Returns
    -------
    str
        UK education level.

    """
    if grade < 2:
        return 'KS1'
    elif grade < 6:
        return 'KS2'
    elif grade < 9:
        return 'KS3'
    elif grade < 11:
        return 'GCSE'
    elif grade < 13:
        return 'A-level'
    else:
        return 'University or higher'
    
def convert_score_to_descriptive(score):
    """
    Function to convert flesch reading-ease score (float) to descriptive
    reading ease (string).

    Parameters
    ----------
    score : float
        Float output by textstat flesch_reading_ease function.

    Returns
    -------
    str
        Descriptive of reading ease.

    """
    
    if score < 10:
        return 'Extremely difficult to read. Professional reading level.'
    elif score < 30:
        return 'Very difficult to read. Graduate reading level.'
    elif score < 50:
        return 'Difficult to read. University student reading level.'
    elif score < 60:
        return 'Fairly difficult to read. A-level reading level.'
    elif score < 80:
        return 'Plain English. GCSE reading level.'
    elif score < 90:
        return 'Easy to read. Conversational English for consumers.'
    else:
        return 'Very easy to read. Easily understood by KS2 students and lower.'

st.title("ONS recruitment - readability scoring")

st.subheader("What is readability?")

st.markdown("Readability refers to how easy a piece of text is to read. There are various different methods for assessing text readability. This tool focuses on two different readability tests, the Flesch reading ease score and the Flesch Kincaid reading grade level.")

st.markdown("Further reading about these two readability tests is avaliable <a href='https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests'>here.</a>", unsafe_allow_html=True)

st.subheader("How to use this app.")

st.markdown("Simply copy and paste the text you want to analyse (e.g. a job advert) into the text box below and press Ctrl+Enter. This will output both a Flesch readability score and a Flesch-Kincaid reading grade level, and compare these to standard UK school reading levels.")

text = st.text_area(label = 'Text to analyse', value = 'Input text to analyse here', height = 300)

reading_ease = tx.flesch_reading_ease(text)
grade_level = tx.flesch_kincaid_grade(text)

reading_ease_descriptive = convert_score_to_descriptive(reading_ease)
grade_descriptive = convert_grade_to_uk_education_level(grade_level)

st.write('Reading ease: {:.2f}. {}'.format(reading_ease, reading_ease_descriptive))
st.write('Grade level: {:.2f}. Equivalent to UK {} reading level.'.format(grade_level, grade_descriptive))