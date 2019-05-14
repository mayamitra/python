import flask
from flask import render_template
app = flask.Flask(__name__)



@app.route("/")
def hello():
	return "<h1>Hello World!</h1>"

# navigation bar 

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

#blog page

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/trial')
def trial():
	return render_template('trial.html')

@app.route('/trial2')
def trial2():
	return render_template('trial2.html')

@app.route("/greet/<name>")
def greet(name):
	return '''
	<h2>Hello, {}! </h2>
		<p> nice day to be happy and relaxed </p>
		'''.format(name)

if __name__ == '__main__':
	app.run(debug=True)