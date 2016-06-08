from flask import render_template
from app import app
import names

@app.route('/')
@app.route('/index')
def index():
	person={'name' : names.get_full_name() }
	return render_template('index.html', user=person)

@app.route('/yolo')
def yo():
	return "Yes"	