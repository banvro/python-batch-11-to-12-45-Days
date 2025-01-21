from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os 
from flask import flash

app = Flask(__name__)

app.secret_key = "lasdbsajdbsad"

db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myblogdb.db"

db.init_app(app)

class ContactUstbl(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    mssage = db.Column(db.Text)
    image_path = db.Column(db.String(120))
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
        my_image = request.files.get("img")

        # print(my_image, "eeeeeeeeee")
        if my_image:
            my_image.save(os.path.join("static/uplodaed_images", my_image.filename))
            path = os.path.join("static/uplodaed_images", my_image.filename)

        user_message = ContactUstbl(username = user_name, email = email, mssage = measge, image_path = path)

        db.session.add(user_message)
        db.session.commit()
        flash("Data Sucessflly saved in Database......", category = "success")
        return redirect("/about") 

    return "data saved sucessfullyy......!"


@app.route("/delete-this-record/<int:my_id>", methods = ['POST'])
def deleterecord(my_id):
    record = ContactUstbl.query.get(my_id)
    # print(record, "eeeeeeeeeeeeeeee")
    db.session.delete(record)
    db.session.commit()

    flash("Record deleted sucessfully...")
    return redirect("/about")


@app.route("/update-record/<int:x>", methods = ["POST"])
def updaterecord(x):
    record = ContactUstbl.query.get(x)
    return render_template("contact_update.html", single_record = record)

@app.route("/update-record-now/<int:my_id>", methods = ["POST"])
def saveUpdateChanges(my_id):
    record = ContactUstbl.query.get(my_id)
    if request.method == "POST":
        user_name = request.form.get("fname")
        email =  request.form.get("email")
        measge = request.form.get("msg")

        record.username = user_name
        record.email = email
        record.mssage = measge

        db.session.commit()

        return redirect("/about")
    return "Changes Saved Sucessfully"

if __name__ == "__main__":
    app.run(port = 1000, debug = True)


