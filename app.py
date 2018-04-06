"""
- DOES: contains backend code for local live demo webpage.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/intervjuer", methods=["GET", "POST"])
def intervjuer():
    return render_template("intervjuer.html")

@app.route("/bloggar", methods=["GET", "POST"])
def bloggar():
    return render_template("bloggar.html")

@app.route("/klassrumsbesok", methods=["GET", "POST"])
def klassrumsbesok():
    return render_template("klassrumsbesok.html")

@app.route("/placeholder_intervju", methods=["GET", "POST"])
def placeholder_intervju():
    return render_template("placeholder_intervju.html")

@app.route("/placeholder_inspirator", methods=["GET", "POST"])
def placeholder_inspirator():
    return render_template("placeholder_inspirator.html")

if __name__ == '__main__':
    app.run()
