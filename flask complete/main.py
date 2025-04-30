from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myflask.db"

db = SQLAlchemy(app)


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    full_name = db.Column(db.String(230))
    email = db.Column(db.String(230))
    phon_number = db.Column(db.String(12))
    messgae = db.Column(db.Text)
    image_path = db.Column(db.String(100))

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



@app.route("/savingdata", methods = ["POST"])
def savethis():
    if request.method == "POST":
        ful_nm = request.form.get("fname")
        em = request.form.get("email")
        pno = request.form.get("pnumber")
        measge = request.form.get("msg")
        img = request.files.get("myimg")

        if img:
            img.save(os.path.join("static", img.filename))
            pathh = os.path.join("static", img.filename)



        data = ContactUs(full_name = ful_nm, email = em, phon_number = pno, messgae = measge, image_path = pathh)

        db.session.add(data)
        db.session.commit()

        return "data savd sucessfully......"

# SQL Alchemy
# 

@app.route("/show")
def showing():
    data = ContactUs.query.all()

    return render_template("showingdata.html", alldata = data)



@app.route("/deletingdata/<int:myxyz>", methods = ["POST"])
def deleting(myxyz):

    data = ContactUs.query.get(myxyz)
    db.session.delete(data)
    db.session.commit()
    return redirect("/show")



@app.route("/updateing/<int:x>")
def updatedata(x):
    data = ContactUs.query.get(x)

    return render_template("updatefrom.html", mydata = data)


@app.route("/saveinfo/<int:x>", methods = ["POST"])
def savinginfo(x):
    data = ContactUs.query.get(x)

    if request.method == "POST":
        ful_nm = request.form.get("fname")
        em = request.form.get("email")
        pno = request.form.get("pnumber")
        measge = request.form.get("msg")

        data.full_name = ful_nm
        data.email = em
        data.phon_number = pno 
        data.messgae = measge

        db.session.commit()

        return redirect("/show")



    return "data updated sucessfulyy........."



if __name__ == "__main__":
    app.run(debug = True)