from flask import Blueprint  


auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>LOGIN</p>"

@auth.route('/logout')
def logout():
    return "<p>LOG-OUT</p>"

@auth.route("/sign-up")
def signup():
    return "<p>SIGN-UP</p>"