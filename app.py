from flask import Flask, request, jsonify
from models import db, User, Transaction
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_tracker.db'
db.init_app(app)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    user = User.query.filter_by(name=data['user']).first()
    if not user:
        user = User(name=data['user'])
        db.session.add(user)
        db.session.commit()
    
    transaction = Transaction(
        user_id=user.id,
        amount=data['amount'],
        category=data['category'],
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        description=data.get('description', '')
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added successfully!'}), 201

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    user_name = request.args.get('user')
    user = User.query.filter_by(name=user_name).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    return jsonify([{
        'amount': t.amount,
        'category': t.category,
        'date': t.date.strftime('%Y-%m-%d'),
        'description': t.description
    } for t in transactions]), 200

if __name__ == '__main__':
    app.run(debug=True)
