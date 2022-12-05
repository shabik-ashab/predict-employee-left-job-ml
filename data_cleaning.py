import pandas

data = pandas.read_csv('HR_comma_sep.csv')

# missing data for any row or any columns
print(data.isnull().values.any())