from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
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
    return render_template("mainpage.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        return redirect('/')


    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    if request.method == 'POST':

        name = request.form.get('username')
        password = request.form.get('password')

        if not name:
            return 'Please input a username'

        if not password:
            return 'Please input password'

        if name != 'go':
            return render_template('login.html')
        elif password != 'ans':
            return render_template('login.html')
            
            
        # Remember which user has logged in
        session["user_id"] = name
            
        return redirect('/')


    # GET
    else:
        return render_template("login.html")


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        return redirect('/')

    else:
        return render_template('profile.html')

@app.errorhandler(404)
def notfound(e):
    return render_template("404.html")



if __name__ == '__main__':
    app.run(debug=True)