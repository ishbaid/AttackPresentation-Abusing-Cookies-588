import os
from flask import Flask, session, render_template, url_for, escape, request, redirect
app = Flask(__name__)

#defaults to true
#setting false allows us to steal the cookie via xss
app.config['SESSION_COOKIE_HTTPONLY'] = False;

@app.route('/')
def index():
	if 'username' in session:
		return redirect(url_for('home')) 
	return redirect(url_for('login'))

@app.route('/home')
def home():
	if 'username' in session:
		message = request.args.get('message')
		if message:
			print message
			print '---------------------'
			return render_template('home.html', message = message)
		else:
			return render_template('home.html')
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/logout')
def logout():
	# remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('index'))

@app.after_request
def kys(response):
	response.headers["X-XSS-Protection"] = 0
	return response
	#print 'afta'

# set the secret key.  keep this really secret:
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.secret_key = os.urandom(24)



































if __name__ == "__main__":
	print "fuuck"
	app.run(debug=True)
