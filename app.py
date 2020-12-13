from flask import Flask, redirect, render_template, request
import attgraph

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')
    graphml = attgraph.graphData(input1, input2)
    
    return render_template('index.html', graphml = graphml)


if __name__ == '__main__':
    app.run(debug=True)
