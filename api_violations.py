

from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/api/users', methods=['GET'])
def get_all_users()

    users = get_users_from_database()
    return json.dumps(users)


@app.route('/api/users', methods=['POST'])
def create_user(
    data = request.get_json()

    user = {
        'name': data.get('name'),
        'email': data.get('email'),
        'password': data.get('password')  # Storing plain text!
    }
    
    save_user(user)
    return {'status': 'success'}


@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if delete_user_from_db(user_id):
        return {'message': 'User deleted'} 
    else:
        return {'error': 'User not found'}, 200  


@app.route('/api/transfer', methods=['POST'])
def transfer_money():
    data = request.get_json()
    try:
        result = process_transfer(data)
        return {'status': 'success'}
    except Exception as e:
  
        return {'error': str(e)}, 500
