from Flask import Flask, flash, redirect, render_template, request, session
from Flask_Session import Session
from Werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps


app = Flask(__name__)

Session(app)

# ensures users are logged in first
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None: 
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@login_required
def index():
    return render_template('mainpage.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':

        name = request.form.get('username')
        password = request.form.get('password')

        if name == 'go' and password == 'pas':
            return redirect('/')

        return render_template('mainpage.html')

    # GET
    else:
        return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)