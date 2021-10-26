import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("./Mall_Customers.csv")

# First we want to see the gender distribution of the customers spending more than average:
customers_with_higher_spending_score = df[df['Spending Score (1-100)'] >= df['Spending Score (1-100)'].mean()]
gender_difference = customers_with_higher_spending_score['Genre'].value_counts(dropna=False)
labels = gender_difference.index.tolist()
fig = plt.figure(figsize=[16, 10])
fig.add_subplot(221)
plt.pie(gender_difference, labels=labels,
        wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
        colors=["#fcbf49", "#98c1d9"], autopct='%1.1f%%',
        startangle=90)
plt.title("Customers with higher spending score gender distribution")

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
fig.add_subplot(222)
plt.pie(age_distr, labels=labels_for_age,
        wedgeprops={'linewidth': 2.0, 'edgecolor': 'white'},
        labeldistance=1.05)
plt.title("Age distribution of customers with higher income and higher spending score")

# we're also interested in customers with higher income: what is their age and if they spend much money in the mall:
df_men = df[df["Genre"] == "Male"]
men_with_higher_income = df_men[df_men['Annual Income (k$)'] >= df_men['Annual Income (k$)'].median()]
df_women = df[df["Genre"] == "Female"]
women_with_higher_income = df_women[df_women['Annual Income (k$)'] >= df_women['Annual Income (k$)'].median()]

x = men_with_higher_income["Spending Score (1-100)"]
y = men_with_higher_income["Age"]

x_w = women_with_higher_income["Spending Score (1-100)"]
y_w = women_with_higher_income["Age"]

fig.add_subplot(223)
plt.scatter(x, y, color='b')
plt.title("Male customers with higher income")
plt.xlabel("Spending Score (1-100)")
plt.ylabel("Age")

fig.add_subplot(224)
plt.scatter(x_w, y_w, color='g')
plt.title("Female customers with higher income")
plt.xlabel("Spending Score (1-100)")
plt.ylabel("Age")

name = "higher_income_cutomers_visualization.png"
plt.savefig(name)

print("\033[032m The file ", name, " has been created\033[0m")