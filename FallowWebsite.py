from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title='Fallow')

@app.route("/farmers")
def farmers():
	return render_template('farmers.html', title='Farmers')

@app.route("/fallowers")
def fallowers():
	return render_template('fallowers.html', title='Fallowers')

@app.route("/leaders")
def leaders():
	return render_template('leaders.html', title='Leaders')

@app.route("/about")
def about():
	return render_template('about.html', title='About Fallow')

if __name__ == '__main__':
	app.run(debug=True)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
