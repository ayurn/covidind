from flask import Flask, render_template, url_for
import requests
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	data = requests.get("https://disease.sh/v2/countries/India?yesterday=true&strict=true")
	data_dict = data.json()
	return render_template("home.html", data = data_dict)

 
if __name__ == "__main__":
	app.debug = True
	app.run()
