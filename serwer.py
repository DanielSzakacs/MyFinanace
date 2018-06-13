from flask import Flask, render_template, request, session, jsonify
app = Flask (__name__)
import database_queri
import hashing
from datetime import datetime
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def main_page():
    #logout()
    # TODO here you have to check if you have a session
    return render_template('login_registration_page.html')


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    username = request.form['username']
    password = request.form['userPassword']
    registration_time = str(datetime.now())
    # TODO checking if the username exsist The query is ""ready""
    hashed_password = hashing.hash_password(password)
    database_queri.save_username(username, hashed_password, registration_time)
    return render_template('login_registration_page.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    hashed_password = database_queri.get_password(username)
    matching = hashing.verify_password(password, hashed_password['password'])
    if matching:
        session["log_in"] = True
        session["username"] = username
        return render_template('account.html')
    else :
        return render_template('login_registration_page.html')


@app.route('/logout')
def logout():
    del session["log_in"]
    del session["username"]
    return render_template("login_registration_page.html")


@app.route('/account')
def account():
    username = session['username']
    time = database_queri.account_get_registration_time(username)
    return render_template('account.html', time=time['registration_time'])


@app.route('/finance')
def finance():
    return render_template('finance.html')


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    currency = request.form['currency']
    income = int(request.form['income'])
    house = int(request.form['house'])
    food = int(request.form['food'])
    cloth = int(request.form['cloth'])
    something = int(request.form['something'])
    year = int(request.form['year'])
    saving = ((income - (cloth + house + food + something)) * 12) * ((2018 - year) * 12)
    return render_template('finance.html', currency=currency, year=year, saving=saving)


if __name__ == "__main__":
    app.run(debug=True,
        port=8000,
        host='0.0.0.0')