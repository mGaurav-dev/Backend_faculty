from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:gaurav1715@localhost:5432/backend_database'
db = SQLAlchemy(app)



@app.route("/")
def index():
    return ("Hii")

@app.route("/homePage")
def homePage():
    return render_template('homePage.html')

@app.route("/viewCertificate")
def viewCert():
    return render_template('viewCertificate.html')

@app.route("/viewMember")
def vieMem():
    return render_template('viewMember.html')

@app.route("/viewActivity")
def viewAct():
    return render_template('viewActivity.html')

@app.route("/viewPending")
def viewPen():
    return render_template('viewPending.html')

# @app.route("/Summary")
# def summary():
#     return render_template('Summary.html')

@app.route("/approveActivity")
def approveAct():
    return render_template('approveActivity.html')

@app.route("/approveCertificate")
def approveCert():
    return render_template('approveCertificate.html')

@app.route("/approveMember")
def approveMem():
    return render_template('approveMember.html')


if __name__ == '__main__':
    app.run(debug=True)
