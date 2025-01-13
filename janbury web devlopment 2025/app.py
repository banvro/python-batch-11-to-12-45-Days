from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///saveForms.db"

db.init_app(app)

class contactus(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    message = db.Column(db.Text)

with app.app_context():
    db.create_all()
    

@app.route("/x")
def homepage():
    return "this is home page.."

@app.route("/z")
def xyz():
    return "this is z page"

@app.route("/")
def homexyz():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contactusX():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/save-this-data", methods = ['POST'])
def datasaving():
    if request.method == "POST":
        fname = request.form.get("fname")
        em = request.form.get("email")
        msg = request.form.get("msg")
        
        # if request.form.get("py") is not None:
        #     print("pyhton is checked...")
        # else:
        #     print("python is not checked")

        my_data = contactus(full_name = fname, email = em, message = msg)

        db.session.add(my_data)
        db.session.commit()

        return redirect("/contact")



if __name__ == "__main__":
    app.run(debug = True, port = 1000)