from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = json.dumps( [1.0,2.0,3.0] )
    labels=json.dumps( ["12-31-18", "01-01-19", "01-02-19"] )
    return render_template('index.html', data=data, labels=labels)