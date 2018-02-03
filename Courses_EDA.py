import pandas as pd
import numpy as np
import matplotlib as np
import json as json

with open('Courses_Tokenized.json') as json_data:
    my_courses = json.load(json_data)
    print(my_courses['301'])

