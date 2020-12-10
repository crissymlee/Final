from flask import Flask, redirect, render_template
import shortest_path

app = Flask(__name__)

@app.route('/')
def index():
    short = 
    return render_template('index.html', short=short)

<<<<<<< Updated upstream
=======
def myDropdown():


>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run()

