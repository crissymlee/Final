from flask import Flask, redirect, render_template, request
import shortest_path

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    print(request.form.get('input1'))
    print(request.form.get('input2'))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
