import pandas as pd
import plotly_express as px
import plotly.graph_objs as go
import seaborn as sns
import plotly.subplots as sp
import streamlit as st
from matplotlib import pyplot as plt

st.title("Mall Customers Dashboard")
df = pd.read_csv("./Mall_Customers.csv")
# st.sidebar.title("Choose your graph")
# radio_button = st.sidebar.radio("Select the visualisation graph:", ('scatter plot', 'seaborn','pie charts'))
# if radio_button == 'scatter plot':


df_low_income = df[df["Annual Income (k$)"]<40]
df_middle_income = df[(df["Annual Income (k$)"]>=40) & (df["Annual Income (k$)"]<70)]
df_high_income = df[df["Annual Income (k$)"]>=70]

fig_1_1 = go.Scatter(y = df_low_income['Spending Score (1-100)'], x = df_low_income['Age'],
	name = "low income", mode = "markers", line = dict(color="green", width=1))
fig_1_2 = go.Scatter(y = df_middle_income['Spending Score (1-100)'], x = df_middle_income['Age'],
	name = "middle income", mode = "markers", line = dict(color="orange", width=1))
fig_1_3 = go.Scatter(y = df_high_income['Spending Score (1-100)'], x = df_high_income['Age'],
	name = "high income", mode = "markers", line = dict(color="blue", width=1))

figures = [fig_1_1, fig_1_2, fig_1_3]
scatter_plot = go.Figure(figures)
scatter_plot.update_layout(title="Spending score relative to Age")
st.plotly_chart(scatter_plot)


df_women = df[df["Genre"] == "Female"]
df_men = df[df["Genre"] == "Male"]
fig_2_1 = go.Histogram(x = df_women['Annual Income (k$)'], name = "female", marker_color='violet')
fig_2_2 = go.Histogram(x = df_men['Annual Income (k$)'], name = "male",  marker_color='mediumpurple')
figures = [fig_2_1, fig_2_2]

histo_plot = go.Figure(figures)
histo_plot.update_layout(title="Income Overview")
histo_plot.update_layout(barmode='stack')
st.plotly_chart(histo_plot)






#Janine's Plots

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
st.plotly_chart(figure)
#figure.savefig("Scatterplot_age_spendingscore.png")
# In this scatter plot I noticed that a part of customers with age <40 have higher spending scores than customers with age >40

# I also create a scatter plot to research the relationship between spending score and income,
# while displaying the difference between male and female
figure = px.scatter(df, Y, Z, color = "Genre")
st.plotly_chart(figure)
# In this scatter plot I noticed that customers with an annual income between 40k and 70k
# have a spending score between 40 and 60. But I cannot make a conclusion about the influence of genre.
# Therefore, I try a different graph: histogram.

figure = px.histogram(df, Z, color="Genre")
st.plotly_chart(figure)
# The histogram shows the difference in spending score between male and female.
# It is obvious that females have a higher spending score than males. Most females have a spending score between 40 and 60.

#Next, I create a scatterplot to visualize the relation between spending score and annual income
# plt.title("Spending score vs Annual Income")
# plt.plot(Z,Y, "ro")
# plt.savefig("Scatterplot_annualincome_spendingscore.png")
#plt.show()
# In this scatter plot I noticed that customers with an annual income between 40k and 70k
# have a spending score between 40 and 60. With this information you can create a target customer group for advertising

# Next, I would like to investigate the relationship between age and spending score a little more.
# From the first plot I already saw that a part of customers with age < 40 have a higher spending score than customers with age>40
# I will use streamlit and plotly graph objects for this purpose.

plot1 = sns.displot(data=df, x="Age", col="Genre", kde=True)
plot2 = sns.jointplot(data=df, kind="scatter", x="Age", y="Spending Score (1-100)", hue="Genre")
st.pyplot(plot1)
st.pyplot(plot2)



#Olga's plots

# First we want to see the gender distribution of the customers spending more than average:
customers_with_higher_spending_score = df[df['Spending Score (1-100)'] >= df['Spending Score (1-100)'].mean()]
gender_difference = customers_with_higher_spending_score['Genre'].value_counts(dropna=False)
labels = gender_difference.index.tolist()
pie = go.Pie(values=gender_difference, labels=labels)
pie_plot = go.Figure([pie])
pie_plot.update_layout(title="Customers with higher spending score gender distribution")
colors = ['gold', 'mediumturquoise']
pie_plot.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.plotly_chart(pie_plot)

# now we want to see the age distribution of the customers spending more than average:
customers_with_higher_Income_and_spending_score = df[
   (df['Spending Score (1-100)'] > df['Spending Score (1-100)'].mean()) & (
         df['Annual Income (k$)'] > df['Annual Income (k$)'].median())]
# filtering data for the new category:
customers_with_higher_Income_and_spending_score.loc[df["Age"] <= 29, "age_range"] = "less than 29"
customers_with_higher_Income_and_spending_score.loc[(df["Age"] >= 30) & (df["Age"] <= 39), "age_range"] = "30-39"
customers_with_higher_Income_and_spending_score.loc[(df["Age"] >= 40) & (df["Age"] <= 49), "age_range"] = "40-49"
customers_with_higher_Income_and_spending_score.loc[(df["Age"] >= 50) & (df["Age"] <= 59), "age_range"] = "50-59"
customers_with_higher_Income_and_spending_score.loc[df["Age"] > 59, "age_range"] = "60+"
age_distr = customers_with_higher_Income_and_spending_score['age_range'].value_counts(dropna=False)
labels_for_age = age_distr.index.tolist()

pie = go.Pie(values=age_distr, labels=labels_for_age)
pie_plot = go.Figure([pie])
pie_plot.update_layout(title="Age distribution of the customers spending more than average")
# define Seaborn color palette to use
colors = sns.color_palette('pastel')
pie_plot.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.plotly_chart(pie_plot)