from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route('/index/<name>')
def hello_world(name):
	return render_template('index.html', name=name)

if __name__ == "__main__":
	print "fuuck"
	app.run()
else:
	print "well"
