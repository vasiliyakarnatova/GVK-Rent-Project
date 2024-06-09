from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ad_page.html")

@app.route("/signin")
def signin():
    return render_template("login.html")

@app.route("/add_property")
def add_property():
    return render_template("AddProperty.html")

@app.route("/agencies")
def agencies():
    return render_template("Agencies.html")

@app.route("/properties")
def properties():
    return render_template("my_properties.html")

if __name__ == "__main__":
    app.run(debug=True)