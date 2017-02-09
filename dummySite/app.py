import os
from flask import Flask, session, render_template, url_for, escape, request, redirect
app = Flask(__name__)

authenticated_users = {}

""" REMOVING DEFENSES """
#defaults to true
#setting false allows us to steal the cookie via xss
app.config['SESSION_COOKIE_HTTPONLY'] = False;

@app.after_request
def kys(response):
	response.headers["X-XSS-Protection"] = 0
	return response

""" DEFENSES REMOVED """

@app.route('/')
def index():
	if 'username' in session or ('mySession' in request.cookies and request.cookies.get('mySession') in authenticated_users):
		return redirect(url_for('home')) 
	return redirect(url_for('login'))

@app.route('/home')
def home():
	if 'mySession' in request.cookies and request.cookies.get('mySession') in authenticated_users:
		message = 'you are logged in with an insecure cookie!'
		return render_template('home.html', message = message, username = authenticated_users[request.cookies.get('mySession')])

	elif 'username' in session:
		message = request.args.get('message')
		if message:
			return render_template('home.html', message = message, username = session['username'])
		else:
			return render_template('home.html', username = session['username'])

	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST' and request.form['password'] == 'asdf':
		
		if 'mySession' in request.cookies:
			authenticated_users[request.cookies.get('mySession')] = request.form['username']

		else:
			session['username'] = request.form['username']
			session['SSN'] = 9001
			session['acct_no'] = 420420420
			session['meaning_of_life'] = 42

		return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	if 'mySession' in request.cookies:
		authenticated_users.pop(request.cookies.get('mySession'), None)
	else:
		session.pop('username', None)
		session.clear()
	return redirect(url_for('index'))

@app.route('/login/fixate', methods=['GET', 'POST'])
def fixatedLogin():
	redirect_to_login = redirect(url_for('login'))
	resp = app.make_response(redirect_to_login)
	sid = request.args.get('sid')
	if sid:
		resp.set_cookie('mySession', value=sid)
	else:
		resp.set_cookie('mySession', value='this_is_a_server_chosen_value_' + os.urandom(12))
	return resp
	

# set the secret key.  keep this really secret:
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.secret_key = os.urandom(24)

if __name__ == "__main__":
	app.run()
