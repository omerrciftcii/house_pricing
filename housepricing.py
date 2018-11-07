import pandas as pd
import numpy as np
from sklearn import datasets,  preprocessing, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def handle_non_numerical_data(df):
    columns = df. columns.values
    for column in columns:
        text_digit_vals = {}

        def convert_to_int(val):
            return text_digit_vals[val]

        if  df[column].dtype != np.int64 and df[column].dtype != np. float64:

            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)

            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1


            df[column] = list(map(convert_to_int, df[column]))
    return df



df = pd .read_csv('housing.csv')

df. fillna(-99999, inplace=True)

df.dropna()

df = handle_non_numerical_data(df)

check = (df.isna())

X_train = np.array(df.drop(['median_house_value'], 1))

y_train = np. array(df['median_house_value'])


X_train, y_train, X_test, y_test = train_test_split(X_train, y_train, test_size=0.2)


print(len(y_train))
'''X_train = preprocessing. scale(X_train)

regression = linear_model.LinearRegression()

regression.fit(X_train, y_train)

regression. fit(X_train, y_train)

y_predict = regression. predict(X_test)

plt. scatter(X_test, y_test, color = 'Black')

plt. plot(X_test, y_predict, color = 'Blue', linewidth = 3)

plt.xticks(())

plt.yticks(())

plt. show()

print("sdsd")

'''