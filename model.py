import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib


data = pd.read_csv('data/sales_data.csv')  
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)


data['Month'] = data.index.month
data['Year'] = data.index.year
data['Day_of_Week'] = data.index.dayofweek


features = ['Month', 'Year', 'Day_of_Week', 'Ad_Spend', 'Price']
target = 'Sales'
X = data[features]
y = data[target]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_train, y_train)


predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")

joblib.dump(model, 'model.pkl')
