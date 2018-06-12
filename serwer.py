from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def main_page():
    # TODO here you have to check if you have a session
    return render_template('mainPage.html')

@app.route("/registration", methods=['POST', 'GET'])
def registration():
    username = request.form['username']
    password = request.fomr['userPassword']

    # TODO finich our registration, and check your sql conection
    return render_template('mainPage.html')

if __name__ == "__main__":
    app.run(debug=True,
        port=8000,
        host='0.0.0.0')