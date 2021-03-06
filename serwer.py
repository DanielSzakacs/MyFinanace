from flask import Flask, render_template, request, session, jsonify, url_for, redirect
app = Flask (__name__)
import database_queri
import hashing
from datetime import datetime
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def main_page():
    logout()
    return render_template('login_registration_page.html')


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    logout()
    username = request.form['username']
    password = request.form['userPassword']
    registration_time = str(datetime.now())
    # TODO checking if the username exsist The query is ""ready""
    hashed_password = hashing.hash_password(password)
    database_queri.save_username(username, hashed_password, registration_time[0:10])
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
        time = database_queri.account_get_registration_time(username)
        return render_template('account.html', time=time['registration_time'])
    else :
        return render_template('login_registration_page.html')


@app.route('/logout')
def logout():
    try:
        del session["log_in"]
        del session["username"]
    except:
        pass
    return redirect(url_for('main_page'))


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
    everything_else = int(request.form['something'])
    year = int(request.form['year'])
    expenditures = cloth + house + food + everything_else
    netto_saving_month = income - expenditures
    saving_month = (income - expenditures) * 12
    saving_year = saving_month * (year - 2018)
    user_id = database_queri.get_user_id(session['username'])
    database_queri.delete_finance_row(user_id['id'])
    database_queri.save_finance_data(user_id['id'], house, food, cloth, everything_else, netto_saving_month)
    return render_template('finance.html', currency=currency, year=year, saving=saving_year)


@app.route('/graph')
def graph():
    user_id = database_queri.get_user_id(session['username'])
    graph_data = database_queri.graph_data(user_id['id'])
    return render_template('grafic.html', data=graph_data[0])


@app.route('/exchange')
def exchange():
    return render_template('exchange.html')


if __name__ == "__main__":
    app.run(debug=True,
        port=8000,
        host='0.0.0.0')