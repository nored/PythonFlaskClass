from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet')
def greet():
    return f"Hello, {request.args['name']}!"

if __name__ == '__main__':
    app.run() 