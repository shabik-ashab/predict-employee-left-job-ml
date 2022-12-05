import pandas as pd

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

data.replace(clean_up_values, inplace=True)
print(data)