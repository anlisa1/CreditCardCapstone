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

@app.route('/research')
def research():
    return render_template('Research.html')

@app.route('/modules')
def courses():
    return render_template('Modules.html')

@app.route('/old_modules')
def old_modules_page():
    return render_template('Modules_backup.html')

@app.route("/modulo<int:id>")
def modulo(id):
  return render_template(f"./modules/modulo{id}.html")

# Here below will be all the original courses link

# @app.route("/module<int:id>")
# def module(id):
#   return render_template(f"./modules/module{id}.html")