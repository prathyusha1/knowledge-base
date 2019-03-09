from flask import render_template, redirect, url_for, request
import sqlite3 as sql

from app import app
from app.helpers.variables import sections

app.secret_key = 'random string'  # used by flash

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['nm']
        password = request.form['pass']
        if username != 'admin' or password != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            return render_template('home.html', sections=sections)
    return render_template('index.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html', sections=sections)

@app.route('/subsection')
def subsection():
    section = request.args.get('section')
    return render_template("subsections.html", section=section, subsections=sections[section]['subsections'], sections=sections)


@app.route('/content')
def content():
    section = request.args.get('section')
    subsection = request.args.get('subsection')
    templatename = section + '/' + subsection + '.html'
    return render_template(templatename, sectionKey=section, sectionName=sections[section]['heading'], heading=sections[section]['subsections'][subsection])
