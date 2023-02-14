from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/resources')
def resources():
    return render_template('Resources.html')

@app.route('/courses')
def courses():
    return render_template('Courses.html')

@app.route('/research')
def research():
    return render_template('Research.html')