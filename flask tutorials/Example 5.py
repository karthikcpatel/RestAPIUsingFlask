from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def customer():
    return render_template('customer.html')


@app.route('/success', methods=['POST', 'GET'])
def print_data():
    if request.method == 'POST':
        result = request.form
        return render_template("result_data.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)