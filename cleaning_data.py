# -*- coding: utf-8 -*-
"""Cleaning_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K1xfd_Gj8WogP3qeXqVkKQkfjFc7iISJ
"""

import numpy as np
import pandas as pd
import re

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/drive/My Drive/machine_learning/philo.csv")
df.head()

print(len(df))

# cleaning title
for i in range(0, len(df)):
    df['Title'].iloc[i] = df['Title'].iloc[i].lower()
    df['Title'].iloc[i] = re.sub(r'\d+s','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\d+','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\'s','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\)','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\(','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\-','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r',','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\.','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r':','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'—','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\"','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\'','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\[','', df['Title'].iloc[i])
    df['Title'].iloc[i] = re.sub(r'\]','', df['Title'].iloc[i])

# cleaning Idea
def CleaningIdea(data):
    for i in range(0, len(data)):
        data['Idea'].iloc[i] = data['Idea'].iloc[i].lower()
        data['Idea'].iloc[i] = re.sub(r'\d+s','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\d+','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\)','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\(','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\-','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r',','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r':','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'—','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\n','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\[','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\]','', data['Idea'].iloc[i])
        # words contractions

        data['Idea'].iloc[i] = re.sub("aren't","are not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("can't","cannot", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("couldn't","could not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("didn't","did not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("doesn't","does not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("don't","do not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("hadn't","had not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("hasn't","has not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("haven't","have not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("he'd","he would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("he'll","he will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("he's","he is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("i'd","i had", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("i'll","i will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("i'm","i am", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("isn't","is not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("it's","it is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("it'll","it will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("i've","i have", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("let's","let us", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("mightn't","might not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("mustn't","must not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("shan't","shall not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("she'd","she would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("she'll","she will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("she's","she is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("shouldn't","should not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("that's","that is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("there's","there is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("they'd","they would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("they'll","they will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("they're","they are", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("they've","they have", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("we'd","we would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("we're","we are", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("weren't","were not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("we've","we have", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("what'll","what will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("where's","where is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("who'd","who would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("who'll","who will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("who're","who are", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("who's","who is", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("who've","who have", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("won't","will not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("wouldn't","would not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("you'd","you would", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("you'll","you will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("you're","you are", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("you've","you have", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("'re"," are", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("wasn't","was not", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("we'll"," will", data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub("tryin'","trying", data['Idea'].iloc[i])

        # others

        data['Idea'].iloc[i] = re.sub(r'\'s','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\"','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(r'\'','', data['Idea'].iloc[i])
        data['Idea'].iloc[i] = re.sub(' +',' ', data['Idea'].iloc[i])
    return data

CleaningIdea(df) # clean all idea data

df.to_csv('/content/drive/My Drive/machine_learning/philo_cleaning.csv', index = False)