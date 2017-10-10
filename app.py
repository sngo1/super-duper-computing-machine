# Team Magic
# Samantha Ngo, Carol Pan
# SoftDev -- pd7
# hw08 -- Do I know you? (pt2)
# 2017-10-06

# Import all necessities
from flask import Flask, render_template, request, session, redirect, url_for
import os

from util import loginMethods

# Create instance of class
app = Flask(__name__) 

# Hard-coded username and password
username = "People"
password = "Cookies"

# Generate secret key to make cookies immutable to others.
app.secret_key = os.urandom(32)

# If initially loading the webpage, load the login page.
# If they're already logged in, then load the welcome page.
@app.route("/")
def loginPage():
    if "username" in session:
        return redirect(url_for("welcome"))     
    else:
        print "loginMethods.login('')"
        return loginMethods.login("")

# Authentification Process
@app.route("/auth", methods=["POST"])
def authentification():
    # Get user-inputted username and password from the form
    userIn = request.form["username"].strip()
    print "U: " + userIn
    passIn = request.form["password"]
    print "P: " + passIn

    # If username and password are correct... 
    if userIn == username and passIn == password:
        # ...open a new session and... 
        session["username"] = username
        # ...render the welcome page by redirecting to login page
        # Login page will recognize that a session is open, so it'll
        # render the welcome page.
        print "URL FOR:", url_for("welcome")
        return redirect(url_for("welcome"))
    # Otherwise, render the login page(again) with an error message.
    else:
        return loginMethods.login("Incorrect username or password")
        
# Logging out renders the login page.
# Should it reroute to the login page instead?
@app.route("/logout")
def logout():
    # End the session
    session.pop("username")
    # Render Login Page
    return loginMethods.login("Logged out!")

@app.route("/welcome")
def welcome():
    if "username" in session:
        print "run loginMethods.loggedIn(session['username'])"
        return loginMethods.loggedIn(session["username"])
    else:
        return redirect(url_for("loginPage"))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
