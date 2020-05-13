from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('Home.html')


@app.route('/testcb', methods=['GET', 'POST'])
def tez():
# try:
    if request.method == 'POST':
	    num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        num3 = int(request.form['num3'])
        num4 = int(request.form['num4'])
        num5 = int(request.form['num5'])
        num6 = int(request.form['num6'])
        sum = num1+num2+num3+num4+num5+num6

        if sum == 231:
            return render_template('Result1.html')
        else:
            return render_template('Result2.html')
    elif request.method == 'GET':
	    return render_template('Test.html')
# except ValueError:
# alert = "Fill in not complete please try again"
# return render_template('test.html', alert=alert)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
