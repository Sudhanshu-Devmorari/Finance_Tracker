import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from models import db, Transaction
from app import app

with app.app_context():
    transactions = Transaction.query.all()

data = [{
    'amount': t.amount,
    'date': t.date
} for t in transactions]

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Resample data to monthly spending
df_monthly = df.resample('M').sum().reset_index()

# Feature engineering
df_monthly['month'] = df_monthly['date'].dt.month
df_monthly['year'] = df_monthly['date'].dt.year

# Prepare data for forecasting
X = df_monthly[['month', 'year']]
y = df_monthly['amount']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict future spending
future_months = pd.DataFrame({
    'month': [8, 9, 10],  # Predicting for August, September, October
    'year': [2024, 2024, 2024]
})

predictions = model.predict(future_months)
print('Predicted spending for the next 3 months:', predictions)
