import pandas as pd
import numpy as np
import json as json
from nltk import word_tokenize
from collections import Counter

# ---------------------------------------------------
def read_courses():
    # Read the CSV file as Pandas Dataframe
    my_courses = pd.read_csv('./Data/Courses.csv')
    return my_courses
# ---------------------------------------------------


# ---------------------------------------------------
def generate_word_tokens(courses):

    my_courses_tokenized = {}
    
    for index, row in courses.iterrows():
        try:
            my_courses_tokenized.update({ row['Course Id'] : word_tokenize(row['Course Description']) })
        except:
            pass

    with open('Courses_Tokenized.json', 'w') as fp:
        json.dump(my_courses_tokenized, fp)

    return True
# ---------------------------------------------------


# generate_word_tokens(read_courses())