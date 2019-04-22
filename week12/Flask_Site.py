import flask
from flask import render_template
app = flask.Flask(__name__)

@app.route("/")
def hello():
	return render_template('home.html')

@app.route("/resume")
def resume():
	return render_template('resume.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/home")
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)