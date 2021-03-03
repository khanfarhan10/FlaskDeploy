from flask import Flask, render_template, request, url_for, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="assets")
ROOT_DIR = os.getcwd()


@app.route('/')
def home():
    return render_template('nav.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/models')
def models():
    return render_template('models.html')


@app.route('/team')
def team():
    return render_template('teams.html')


@app.route('/net')
def net():
    return render_template('coviddeepnet.html')


@app.route('/shreya')
def shreya():
    return render_template('shreya.html')


@app.route('/custommodels')
def custom_models():
    return render_template('custom_model.html')

@app.route('/damik')
def damik():
    return render_template('damik.html')


if __name__ == "__main__":
    app.run(debug=True)
