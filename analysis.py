import pandas as pd
import matplotlib.pyplot as plt
from models import db, Transaction
from app import app

with app.app_context():
    transactions = Transaction.query.all()

data = [{
    'amount': t.amount,
    'category': t.category,
    'date': t.date,
    'user': t.user.name
} for t in transactions]

df = pd.DataFrame(data)

# Total spending by category
category_spending = df.groupby('category')['amount'].sum()
category_spending.plot(kind='pie', autopct='%1.1f%%')
plt.title('Spending by Category')
plt.show()

# Time series analysis of spending
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df['amount'].resample('M').sum().plot(kind='line')
plt.title('Monthly Spending')
plt.show()
