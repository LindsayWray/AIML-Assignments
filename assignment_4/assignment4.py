# import pandas as pd
# import pandas_profiling as pp

# df = pd.read_csv("Mall_Customers - Mall_Customers.csv")
# print(df.info()) # shows that there are no null values
# profile = pp.ProfileReport(df)
# profile.to_file("Mall_Customers - Mall_Customers.csv")

# df_women = df[df["Genre"]=="Female"]
# profile_women = pp.ProfileReport(df_women)
# profile_women.to_file("Mall_Customers - Mall_Customers_Women.csv")

# #There doesn't seem to be much differences between male and female mall customers



# df.loc[df["Annual Income (k$)"]<40,"income_cat"] = "low income"
# df.loc[(df["Annual Income (k$)"]>=40)&(df["Annual Income (k$)"]<70),"income_cat"] = "average income"
# df.loc[df["Annual Income (k$)"]>=70,"income_cat"] = "high income"
# mean_income = df.groupby("income_cat")["Spending Score (1-100)"].mean()
# print("\nThe mean spending score of different income groups:\n", mean_income)
# median_income = df.groupby("income_cat")["Spending Score (1-100)"].median()
# print("\nThe median spending score of different income groups:\n", median_income)

# There doesn't seem to be any difference in the average spending score based on income

import pandas as pd
import pandas_profiling as pp

df = pd.read_csv("Mall_Customers - Mall_Customers.csv")

print("\033[033mHow many customers of different genders visit the mall:\033[0m")
print(df['Genre'].value_counts(dropna=False))

#there appears to be more female mall visitors than the male ones

print("\033[033mSpending score in the men category:\033[0m")
print("MAX SPENDING SCORE -  MALE: ", df['Spending Score (1-100)'][df['Genre'] == "Male"].max())
print("MAX INCOME - MALE: ", df['Annual Income (k$)'][df['Genre'] == "Male"].max())
print("MIN SPENDING SCORE  - MALE: ", df['Spending Score (1-100)'][df['Genre'] == "Male"].min())
print("MIN INCOME  - MALE: ", df['Annual Income (k$)'][df['Genre'] == "Male"].min())
print("SPENDING SCORE - MEDIAN - MALE: ", df['Spending Score (1-100)'][df['Genre'] == "Male"].median())
print("\033[033mSpending score in the women category:\033[0m")
print("MAX SPENDING SCORE FEMALE: ", df['Spending Score (1-100)'][df['Genre'] == "Female"].max())
print("MAX INCOME FEMALE: ", df['Annual Income (k$)'][df['Genre'] == "Female"].max())
print("MIN SPENDING_ CORE FEMALE: ", df['Spending Score (1-100)'][df['Genre'] == "Female"].min())
print("MIN INCOME FEMALE: ", df['Annual Income (k$)'][df['Genre'] == "Female"].min())
print("Median FEMALE: ", df['Spending Score (1-100)'][df['Genre'] == "Female"].median())

#There doesn't seem to be much differences between male and female mall customers


df.loc[df["Annual Income (k$)"]<40,"income_cat"] = "low income"
df.loc[(df["Annual Income (k$)"]>=40)&(df["Annual Income (k$)"]<70),"income_cat"] = "average income"
df.loc[df["Annual Income (k$)"]>=70,"income_cat"] = "high income"
mean_income = df.groupby("income_cat")["Spending Score (1-100)"].mean()
print("\n\033[033mThe mean spending score of different income groups:\033[0m\n", mean_income)
median_income = df.groupby("income_cat")["Spending Score (1-100)"].median()
print("\n\033[033mThe median spending score of different income groups:\033[0m\n", median_income)

#Let's create profile report to visua;ize our data:
df_women = df[df["Genre"]=="Female"]
df_men = df[df["Genre"]=="Male"]

profile_both = pp.ProfileReport(df)
profile_women = pp.ProfileReport(df_women)
profile_men = pp.ProfileReport(df_men)
profile_both.to_file("profile_both_genders.html")
profile_women.to_file("women_profile_file.html")
profile_men.to_file("men_profile_file.html")