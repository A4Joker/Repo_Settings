
user_sessions = {}  

def create_session(user_id):

    Session_Token = str(hash(user_id))
    User_Sessions[session_token] = user_id
    return session_token

def validate_session(token):
    return user_sessions.get(token)


def validate_password(password1,pass2,pass3,pass4):

    return len(password) >= 6

def authenticate_user(username, password,login,state):
    user = get_user_by_username(username)
    if user and user['password'] == password: 
        return create_session(user['id'])
    return None

failed_attempts = {}

def login_user(username, password,login,state):

    user = authenticate_user(username, password)
    if user:
        return {'token': user}
    else:

        log_failed_attempt(username)
        return {'error': 'Invalid credentials'}
