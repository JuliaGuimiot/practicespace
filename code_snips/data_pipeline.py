# Scraping raw data from multiple sources (including web and database tables)
# Imputing, formatting, and transforming – basically making it ready to be used
# Handling read/write errors
# Detecting outliers
# Performing quick visualizations (plotting) and basic statistical analysis to judge the quality of your formatted data

# built-in data types - Lists, Sets, Strings, Tuples, and Dictionaries

# ITERATOR
# We will start off this topic with lists. However, before we get into lists, we will introduce the concept of an iterator. An iterator is an object that implements the next method, meaning an iterator is an object that can iterate over a collection (lists, tuples, dicts, and so on). It is stateful, which means that each time we call the next method, it gives us the next element from the collection. And if there is no further element, then it raises a StopIteration exception.
#
# Note
# A StopIteration exception occurs with the iterator's next method when there are no further values to iterate.
#
# If you are familiar with a programming language like C, C++, Java, JavaScript, or PHP, you may have noticed the difference between the for loop implementation in those languages, which consists of three distinct parts, precisely the initiation, the increment, and the termination condition, and the for loop in Python. In Python, we do not use that kind of for loop. What we use in Python is more like a foreach loop: for i in list_1. This is because, under the hood, the for loop is using an iterator, and thus we do not need to do all the extra steps. The iterator does this for us.
import pandas as pd
import sqlite3
# connect to the database - if it doesn't exist, create it
data = pd.read_csv('Food_Establishment_Inspection_Scores.csv')
data.drop('Facility ID',axis=1,inplace=True)
print(data.head)

# print(data.sample(10))
# print(data.shape)
# missing_values_count = data.isnull().sum()
# print(missing_values_count)
# connection = sqlite3.connect('salaries_by_college_type.db')
# connection.close()
