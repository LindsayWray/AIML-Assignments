# Assignment 5
# Janine Simons October 25 2021
# Perform advanced level data visualisation using plotly and seaborn to project charts
# on to streamlit app for dataset provided for assignment 4.
# Make min of 3 different visualisations.

import pandas as pd
import pandas_profiling as pp
from matplotlib import pyplot as plt
import seaborn as sns
import plotly_express as px
import streamlit as st

#profile = pp.ProfileReport(df)
#profile.to_file("Summaryreport.html")

df = pd.read_csv("Mall_Customers.csv")
print(df.info())
print(df.describe())
X = df["Age"]
Y = df["Annual Income (k$)"]
Z = df["Spending Score (1-100)"]
S = df["Genre"].value_counts()

# First I create simple scatter plot to research the relation between spending score and age,
# where I try to display the difference between male and female
# Initially I used the scatter function of plotly express for this purpose
figure = px.scatter(df, X, Z, color = "Genre")
figure.show()
#figure.savefig("Scatterplot_age_spendingscore.png")
# In this scatter plot I noticed that a part of customers with age <40 have higher spending scores than customers with age >40

# I also create a scatter plot to research the relationship between spending score and income,
# while displaying the difference between male and female
figure = px.scatter(df, Y, Z, color = "Genre")
figure.show()
# In this scatter plot I noticed that customers with an annual income between 40k and 70k
# have a spending score between 40 and 60. But I cannot make a conclusion about the influence of genre.
# Therefore, I try a different graph: histogram.

figure = px.histogram(df, Z, color="Genre")
figure.show()
# The histogram shows the difference in spending score between male and female.
# It is obvious that females have a higher spending score than males. Most females have a spending score between 40 and 60.

#Next, I create a scatterplot to visualize the relation between spending score and annual income
plt.title("Spending score vs Annual Income")
plt.plot(Z,Y, "ro")
plt.savefig("Scatterplot_annualincome_spendingscore.png")
#plt.show()
# In this scatter plot I noticed that customers with an annual income between 40k and 70k
# have a spending score between 40 and 60. With this information you can create a target customer group for advertising

# Next, I would like to investigate the relationship between age and spending score a little more.
# From the first plot I already saw that a part of customers with age < 40 have a higher spending score than customers with age>40
# I will use streamlit and plotly graph objects for this purpose.


