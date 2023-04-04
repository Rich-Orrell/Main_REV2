from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
import mysql.connector


# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = "123123"
# app.config['MYSQL_DB'] = "ncstdb"
# conn = MySQL(app)


# connecting the database
conn = mysql.connector.connect(host="localhost", user="root", passwd="123123", database="ncstdb")
db = conn.cursor()

# Standard practice to create a flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'


# setting up client to server views, each view is connected to and HTML page
@app.route("/")
def base():
    return render_template("index.html")


@app.route("/homepage")
def hompage():
    return render_template("homepage.html")


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        db.execute("SELECT username, password FROM users")
        user = db.fetchone()
        print(user)
        print(username)
        if user == (username, password):
            print('succs')

            return render_template('admin.html')
        else:
            flash('Incorrect username or password, try again.', category='error')
            print('failed')
            return render_template('login.html')

    return render_template('login.html')


@app.route("/report-vulnerabilities", methods=['GET', 'POST'])
def reportv():

    if request.method == 'POST':
        firstname = request.form['fname']
        lastname = request.form['lname']
        email_address = request.form['email']
        data_time = request.form['dtg']
        domain_link = request.form['vweb']
        age = request.form['age']
        username = request.form['uname']
        v_d = request.form['vd']
        v_s = request.form['vs']
        print(firstname)
        return render_template("homepage.html")
    else:
        return render_template("reportv.html")


@app.route("/current-vulnerabilities")
def currentv():
    return render_template("currentv.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/userinfo")
def userinfo():
    return render_template("userinfo.html")


# standard practice to run flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

