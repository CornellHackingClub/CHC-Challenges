from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user 
from datetime import timedelta
import os

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'LOLOLOL_I_Am_So_Secret'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = 'CHC'
        self.password = 'OverErryThing'
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

users = [User(1)]

# some protected url
@app.route('/')
@login_required
def home():
    response = render_template('home.html', name=home)
    if session.get('_flashes'): del session['_flashes']
    if session.get('user_id'): del session['user_id']
    if session.get('_fresh'): del session['_fresh']
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)
    session['Flag'] =  os.e#make env variable
    return response

 
# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print username
        print password 
        if password == 'OverErryThing' and username == 'CHC':
            user = User(1)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return render_template('login.html', name=login)


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return render_template('fail.html')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)
