from flask import Flask, render_template, request
app = Flask (__name__)
import database_queri
import hashing

@app.route('/')
def main_page():
    # TODO here you have to check if you have a session
    return render_template('login_registration_page.html')


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    username = request.form['username']
    password = request.form['userPassword']
    # TODO checking if the username exsist The query is ""ready""
    hashed_password = hashing.hash_password(password)
    database_queri.save_username(username, hashed_password)
    return render_template('main_page.html')


if __name__ == "__main__":
    app.run(debug=True,
        port=8000,
        host='0.0.0.0')