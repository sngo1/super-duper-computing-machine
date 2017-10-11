# Team Magic
# Samantha Ngo, Carol Pan
# SoftDev -- pd7
# hw08 -- Do I know you? (pt2)
# 2017-10-06

# Import all necessities
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for
from flask import flash
import os

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
        return render_template("login.html")

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
        print "Matches data in database"
        print "URL FOR:", url_for("welcome")
        flash( "Success!" )
        return redirect(url_for("welcome"))
    # Otherwise, render the login page(again) with an error message.
    else:
        print "Does not match"
        flash( "Incorrect Username or Password Given!" )
        return render_template("login.html")
        
# Logging out renders the login page.
# Should it reroute to the login page instead?
@app.route("/logout")
def logout():
    # End the session
    session.pop("username")
    print "User has logged out"
    # Render Login Page
    flash( "You have logged out!" )
    return redirect(url_for("loginPage"))

@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_template("welcome.html")
    else:
        return redirect(url_for("loginPage"))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
