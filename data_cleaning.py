import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('HR_comma_sep.csv')

# missing data for any row or any columns
# print(data.isnull().values.any())

# check data type
# print(data.dtypes)

# print(data.salary.unique())
# print(data.Department.unique())

clean_up_values = {
    'salary':{
        'low': 1,
        'medium': 2,
        'high': 3
    }
}

# dummies for department
data.replace(clean_up_values, inplace=True)
# print(data)

dummies = pd.get_dummies(data.Department)
# print(dummies)

# merge dummy column with original data 
merged = pd.concat([data, dummies], axis='columns')
# print(merged)

# drop unnessery columns
final_data = merged.drop(['Department'], axis='columns')
# print('Department' in list(final_data.columns))

# show data on a scatter plot
# plt.scatter(x=final_data.salary, y=final_data.left)
# plt.scatter(x=final_data.satisfaction_level, y=final_data.left)
plt.scatter(x=final_data.time_spend_company, y=final_data.left)
plt.show()