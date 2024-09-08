# Personal Finance Tracker with Budget Forecasting

This project is a personal finance tracker that allows users to manage their finances by tracking income, expenses, and savings. It also provides budget forecasting based on historical financial data using simple machine learning models.

## Features

- **Track Income & Expenses**: Add, view, and categorize transactions.
- **Budget Forecasting**: Predict future spending based on past data using linear regression.
- **Data Visualization**: Visualize financial data, such as total spending by category and monthly spending trends.
- **User Management**: Simple user profiles to manage individual financial data.

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (can be swapped with PostgreSQL)
- **Data Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib
- **Frontend**: Simple API (optional web interface)

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Budget Forecasting](#budget-forecasting)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/finance-tracker.git
    cd finance-tracker
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the SQLite database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

## Database Setup

The project uses SQLite for simplicity. You can configure PostgreSQL by updating the `SQLALCHEMY_DATABASE_URI` in `app.py`.

For SQLite:

- The database file will be created automatically when the app is first run.
- You can view and manage the database using a tool like DB Browser for SQLite.

## Usage

### Adding Transactions

You can add transactions (income/expenses) using the `/add_transaction` API endpoint. Here's a sample request body in JSON format:

```json
{
  "user": "John Doe",
  "amount": 250.75,
  "category": "Groceries",
  "date": "2024-08-25",
  "description": "Weekly grocery shopping"
}
