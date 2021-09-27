
def verify_is_user(response):
    return 'username' in response

def verify_is_user_registered(resposne):
    return 'errors' not in resposne

def verify_is_email_reseted(resposne):
    return 'success' in resposne

def handler_login_error(response, form):
    for error in response:
        form.add_error('password', response[error])

def handler_register_error(response, form):
    for error in response['errors']:
        form.add_error('password', response['errors'][error])

def handler_reset_password_error(response, form):
    for error in response:
        form.add_error('email', response[error])