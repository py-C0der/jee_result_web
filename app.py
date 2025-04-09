from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/session1')
def session1():
    return render_template('session1.html')

@app.route('/session2')
def session2():
    return render_template('session2.html')

if __name__ == '__main__':
    app.run(debug=True)
