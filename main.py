from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    if 'name' in request.args:
        name = request.args['name']
    else:
        name = None
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run() 