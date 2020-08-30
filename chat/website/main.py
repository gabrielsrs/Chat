# make a web server, to make a GUI to receive the messages

# page with when pop up begin ask your name adn put into from chat room(1 leave and another enter)
from flask import Flask, render_template, url_for

Name_key = "name"

app = Flask(__name__)
app.secret_key = "hellomyname'sGabriel"


"""
@app.route("/login")
def login():
    return render_template("login.html")"""


@app.route("/logout")
def logout():
    session.pop(Name_key, None)
    return redirect(url_for("login"))


@app.route("/")
@app.route("/home")
def home():
#    if Name_key not in session:
#        redirect(url_for("login"))

#    name = session[Name_key]
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
