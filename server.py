from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_bootstrap import Bootstrap
import os
import imp
import sys

# Append custom python directoy to path
sys.path.append('/home/ubuntu/HackCooper2016/py/')
import helper_fns # Custom functions for make_problem
import make_project # Generate code problem

app = Flask(__name__)
Bootstrap(app)

@app.route("/css/<path:path>",methods=['GET'])
def css(path):
    return send_from_directory('css',path)

@app.route("/fonts/<path:path>",methods=['GET'])
def fonts(path):
    return send_from_directory('fonts',path)

@app.route("/js/<path:path>",methods=['GET'])
def js(path):
    return send_from_directory('js',path)

# Return home screen
@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

# Return text field
@app.route('/text', methods=['GET','POST'])
def text():
    return render_template('text_area.html',
        success = 'none',
        stdout = 'none',
        error  = 'none')

# Check if code is right
@app.route('/check',methods=['GET','POST'])
def checkCode():
    code     = str(request.form['value'])
    language = str(request.form['lang'])
    problem  = str(request.form['prob'])
    output = helper_fns.runProblemJson(problem,code)
    if output['exit'] == 0:
        error = True
    else:
        error = False
    return render_template('text_area.html',
        success = output['correct'],
        stdout = output['stdout'],
        error  = error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
