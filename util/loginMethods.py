from flask import Flask, render_template

def login(message):
    return render_template('login.html',
                               msg = message)
def loggedIn(username):
    return render_template('welcome.html',
                               username = username)
