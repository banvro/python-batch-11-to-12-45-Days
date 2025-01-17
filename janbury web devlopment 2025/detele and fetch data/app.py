from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myblogdb.db"

db.init_app(app)

class ContactUstbl(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    mssage = db.Column(db.Text)
    message_date = db.Column(db.String, default=datetime.now())

with app.app_context():
    db.create_all()


@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/about")
def aboutthis():
    my_records = ContactUstbl.query.all()[::-1]
    # print(records)
    return render_template("about.html", records = my_records)

@app.route("/contact")
def contactus():
    return render_template("contact.html")

@app.route("/services")
def myservices():
    return render_template("services.html")

@app.route("/savingdata", methods = ['POST'])
def savingdata():
    if request.method == "POST":
        user_name = request.form.get("fname")
        email =  request.form.get("email")
        measge = request.form.get("msg")

        user_message = ContactUstbl(username = user_name, email = email, mssage = measge)

        db.session.add(user_message)
        db.session.commit()
        return redirect("/about") 

    return "data saved sucessfullyy......!"


@app.route("/delete-this-record/<int:my_id>", methods = ['POST'])
def deleterecord(my_id):
    record = ContactUstbl.query.get(my_id)
    # print(record, "eeeeeeeeeeeeeeee")
    db.session.delete(record)
    db.session.commit()
    return redirect("/about")

if __name__ == "__main__":
    app.run(port = 1000, debug = True)


