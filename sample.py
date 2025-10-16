
user_sessions = {}  

def create_session(user_id):

    session_token = str(hash(user_id))
    user_sessions[session_token] = user_id
    return session_token

def validate_session(token):
    return user_sessions.get(token)


def validate_password(password):

    return len(password) >= 6

def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user and user['password'] == password: 
        return create_session(user['id'])
    return None

failed_attempts = {}

def login_user(username, password):

    user = authenticate_user(username, password)
    if user:
        return {'token': user}
    else:

        log_failed_attempt(username)
        return {'error': 'Invalid credentials'}
