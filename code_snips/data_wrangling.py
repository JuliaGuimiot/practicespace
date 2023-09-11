## Data Wrangling and Databases

# 1. Case study scenario
# 2. Step-by-step concept breakdown and code examples
# 3. Practice exercises
# 4. Further practice and applications


# 1. Case Study Scenario
# We want to find the best restaurants in Austin based on geographical location, and their health department inspection rating.
#
# So, we will need to find applicable data and aggregate it into a searchable format.
# In this case, we're going to use data from the City of Austin
# (https://data.austintexas.gov/Health-and-Community-Services/Food-Establishment-Inspection-Scores/ecmv-9xxi).
# They offer both an API, and a downloadable csv file of their Food Establishment Inspection Scores database

# 2.
# Specific steps:
# Examine the database online:
# what data is present?
# is the data present complete, or are there blank sections?

# Tools:
# To best examine the data locally, we're going to use the pandas library,
# which is designed to let users manipulate and analyze data in Python.

# Then, once we are satisfied with the data we have, we'll use the built in sqlite3 module
# to quickly create a sqlite database

#

import pandas as pd
from sodapy import Socrata

data = pd.DataFrame.read_csv('Food_Establishment_Inspection_Scores.csv')
# data.sample(10)

# print(data.columns.values)

# Where is there data missing or unavilable?

# missing_values_count = data.isnull().sum()
# print(missing_values_count)


# API code
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.austintexas.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.austintexas.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# results = client.get("ecmv-9xxi", limit=2000)

# Convert to pandas DataFrame
# results_df = pd.DataFrame.from_records(results)
#
# import sqlite3
# connection = sqlite3.connect('housing.db')
#
# my_cursor = connection.cursor()
#
# my_cursor.execute("""
# CREATE TABLE ca_housing (
#   longitude real,
#   latitude real,
#   housing_median_age real,
#   total_rooms real,
#   total_bedrooms real,
#   population real,
#   households real,
#   median_income real,
#   median_house_value real
# )""")
#
# connection.commit()
#
# my_cursor.execute("INSERT INTO ca_housing VALUES (-118.04,	33.95,	36.0,	1976.0,	368.0,	1236.0,	355.0,	4.6150,	174000.0)")
#
# my_cursor.execute("SELECT * FROM ca_housing")
#
# print(my_cursor.fetchall())
# # single element from db returns as a tuple, multiple returns as a list of tuples
#
# connection.close()
#
# def show_all():
#   connection = sqlite3.connect('housing.db')
#   cur = connection.cursor()
#
#   cur.execute("SELECT * FROM ca_housing")
#   items = cur.fetchall()
#
#   for item in items:
#     print(item)
#
#   connection.commit()
#   connection.close()
#
# def add_one(longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income real, median_house_value):
#   connection = sqlite3.connect('housing.db')
#   cur = connection.cursor()
#
#   cur.execute("INSERT INTO ca_housing VALUES (?,?,?,?,?,?,?,?,?)", (longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income real, median_house_value))
#
#   connection.commit()
#   connection.close()
