from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return Simple 'Welcome'"""
    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def say_welcome_home():
    """Return Simple 'Welcome home'"""
    html = "<html><body><h1>Welcome home</h1></body></html>"
    return html   

@app.route('/welcome/back')
def say_welcome_back():
    """Return Simple 'Welcome back'"""
    html = "<html><body><h1>Welcome back</h1></body></html>"
    return html 