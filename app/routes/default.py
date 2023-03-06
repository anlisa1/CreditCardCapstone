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

# Here below will be all the original courses link

@app.route('/module1')
def module1():
    return render_template('./modules/module1.html')

@app.route('/module2')
def module2():
    return render_template('./modules/module2.html')

@app.route('/module3')
def module3():
    return render_template('./modules/module3.html')

@app.route('/module4')
def module4():
    return render_template('./modules/module4.html')

@app.route('/module5')
def module5():
    return render_template('./modules/module5.html')

@app.route('/module6')
def module6():
    return render_template('./modules/module6.html')

@app.route('/module7')
def module7():
    return render_template('./modules/module7.html')

@app.route('/module8')
def module8():
    return render_template('./modules/module8.html')

@app.route('/module9')
def module9():
    return render_template('./modules/module9.html')