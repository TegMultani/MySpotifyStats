from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    
    # Check if logged in, if true then change Login buttons to "Account" and "View Stats"


    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)