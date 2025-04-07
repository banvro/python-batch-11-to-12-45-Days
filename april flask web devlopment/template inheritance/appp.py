from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def aboutpage():
    return render_template("about.html")

@app.route("/contact")
def contactpage():
    return render_template("contact.html")








if __name__ == "__main__":
    app.run(port = 1000, debug = True)

    