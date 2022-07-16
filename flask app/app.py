from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


app = Flask(__name__)

# # ensures users are logged in first
# def login_required(f):
#     """
#     Decorate routes to require login.

#     https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
#     """
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("user_id") is None: 
#             return redirect("/login")
#         return f(*args, **kwargs)
#     return decorated_function


@app.route("/")
def index():
    return render_template('mainpage.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return render_template('mainpage.html')
    else:
        return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True)