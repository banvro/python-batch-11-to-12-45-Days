from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myflask.db"

db = SQLAlchemy(app)


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(230))
    email = db.Column(db.String(230))
    phon_number = db.Column(db.String(12))
    messgae = db.Column(db.Text)

with app.app_context():
    db.create_all()



@app.route("/")
def hompage():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


# SQL Alchemy
# 

if __name__ == "__main__":
    app.run(debug = True)