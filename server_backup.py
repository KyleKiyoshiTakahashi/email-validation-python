from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "WHAT"
from mysqlconnection import connectToMySQL

@app.route('/')

def route():

    return render_template("index.html")
    # emailaddress = emailusers )

@app.route('/process',methods=['POST'])

def process():
    ## validation
    ## if it doesn't validate go back to index
    ### if it does go to success 
    #### regex
    ##### add errors to flash
    ####### errors appear in index 
    # emailusers = mysql.query_db('SELECT * FROM users')
        # if this statement comes back 
    if len(request.form['emailaddress']) == 0:
        flash("Email is not valid")
        return redirect('/')

    mysql = connectToMySQL('email_digest')
    query = "INSERT INTO users(email, created_at, update_at) VALUES(%(email)s, NOW(),NOW());"
    data = {"email": request.form['emailaddress']} 
    mysql.query_db(query,data)
    session["recentEmail"] = request.form['emailaddress']

    return redirect('/success')

@app.route('/success')

def success():
    mysql = connectToMySQL('email_digest')
    query = "SELECT email, created_at FROM users" # we only need the email address
    all_emails = mysql.query_db(query)


    return render_template("success.html", emails = all_emails)

    # goes to render 
    


if __name__=='__main__':
    app.run(debug=True)

