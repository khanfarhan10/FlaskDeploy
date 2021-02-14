from flask import Flask, render_template, request, url_for, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="assets")
ROOT_DIR = os.getcwd()

@app.route('/')
def home():
    return render_template('nav.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/team')
def team():
    return render_template('teams.html')

if __name__=="__main__":
    app.run(debug=True)