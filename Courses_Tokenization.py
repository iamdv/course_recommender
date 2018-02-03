import pandas as pd
import numpy as np
from nltk import word_tokenize
from collections import Counter

# Read the CSV file as Pandas Dataframe
my_courses = pd.read_csv('./Data/Courses.csv')

my_courses_tokenized = {}

for index, row in my_courses.iterrows():
    try:
        my_courses_tokenized.update({ row['Course Id'] : word_tokenize(row['Course Description']) })
    except:
        pass

print(my_courses_tokenized)

