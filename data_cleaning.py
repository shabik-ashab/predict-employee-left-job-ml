import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
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
# plt.scatter(x=final_data.time_spend_company, y=final_data.left)
# plt.show()

x = final_data.drop('left', axis='columns')
y = final_data.left

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression()
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print(accuracy)

# confusion matrics
y_predicted = model.predict(x_test)
confusion = confusion_matrix(y_test, y_predicted)
# print(confusion)

plot_confusion_matrix(model, x_test, y_test)
plt.show()




