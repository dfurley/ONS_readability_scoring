# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:10:45 2022

@author: furled
"""

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