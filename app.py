# Team Magicians
# Samantha Ngo, Carol Pan
# SoftDev -- pd7
# hw08 -- Do I know you? (pt2)
# 2017-10-06

# Import all necessities
from flask import Flask, render_template, request, session, redirect, url_for
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
def login():
    print "Session.get('Jeff') returns ", session.get("Jeff")
    if "username" in session:
        return render_template('welcome.html',
                               username = session["username"])
    else:
        return render_template('login.html',
                               msg = "")

# Authentification Process
@app.route("/auth", methods=["POST"])
def authentification():
    # Get user-inputted username and password from the form
    userIn = request.form["username"]
    print "U: " + userIn
    passIn = request.form["password"]
    print "P: " + passIn

    # If username and password are correct... 
    if userIn == username and passIn == password:
        # ...open a new session and...
        session["username"] = userIn
        # ...render the welcome page.
        # return render_template("welcome.html",
        #                       username = session["username"])
        print "URL FOR:", url_for("login")
        return redirect(url_for("login"))
    # Otherwise, render the login page(again) with an error message.
    else:
        return render_template("login.html",
                               msg = "Incorrect username or password.")

# Logging out renders the login page.
# Should it reroute to the login page instead?
@app.route("/logout")
def logout():
    # End the session
    session.pop("username")
    # Render Login Page
    return render_template("login.html",
                            msg = "Logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
