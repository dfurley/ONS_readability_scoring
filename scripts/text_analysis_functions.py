# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:10:45 2022

@author: furled
"""

import re

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

def format_text_for_flesch_kincaid (text):
    """
    Formats text for FK scoring. Removes line breaks, punctuation and ellipses.

    Parameters
    ----------
    text : TYPE
        Unformatted text.

    Returns
    -------
    text : TYPE
        Formatted text.

    """
    # remove line breaks and replace with full stops, then replace question marks and ellipses with full stops
    text = text.replace("\n", ".")
    text = text.replace("?", ".")
    text = text.replace("...", ". ")
    text = text.replace("..", ". ")
    text = text.replace(" .", "")
    
    # lowercase text
    text = text.lower()
    
    
    # remove punctuation
    text = re.sub('[^a-zA-Z0-9 \n\.]', ' ', text)
    
    return text

def word_syllable_count(word):
    """
    Function to count syllables in a word

    Parameters
    ----------
    word : string
        DESCRIPTION.

    Returns
    -------
    count : int
        Count of syllables in a given word.

    """
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if word.endswith("le"):
        count += 1
    if count == 0:
        count += 1
    return count

def text_syllable_count(words):
    """
    Function to count all syllables in a text

    Parameters
    ----------
    words : list
        List of words from text, found using word_tokenize.

    Returns
    -------
    count : int
        Count of syllables from entire text.

    """
    count = 0
    
    for word in words:
        count += word_syllable_count(word)
        
    return count

def list_long_words(words):
    """
    Function to return lists of 3, 4 and 5+ syllable words

    Parameters
    ----------
    words : list
        word tokens from text.

    Returns
    -------
    word_dict : dictionary
        dictionary of 3 different list, containing 3, 4 and 5+ syllable words.

    """
    word_dict = {}
    
    three_syllable_words = []
    four_syllable_words = []
    five_plus_syllable_words = []
    
    for word in words:
        if word_syllable_count(word) >= 5:
            five_plus_syllable_words.append(word)
        elif word_syllable_count(word) >= 4:
            four_syllable_words.append(word)
        elif word_syllable_count(word) >= 3:
            three_syllable_words.append(word)
    
    word_dict['three_syllables'] = three_syllable_words
    word_dict['four_syllables'] = four_syllable_words
    word_dict['five_plus_syllables'] = five_plus_syllable_words
    
    return word_dict    