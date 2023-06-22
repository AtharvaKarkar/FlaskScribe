from flask import Blueprint,render_template  # blueprint is a way to organize and structure a web application into reusable components


views = Blueprint('views',__name__) # defining a blue print

@views.route('/')
def home():
    return render_template("home.html")         # 'pass' statement is a placeholder that does nothing.It is just used when a statement that is syntatically required, used as a temporary placeholder for code that will be implemented later.