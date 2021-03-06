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

################################################################################
# interviews START:
################################################################################
@app.route("/placeholder_intervju", methods=["GET", "POST"])
def placeholder_intervju():
    return render_template("placeholder_intervju.html")

@app.route("/anton_borgstrom", methods=["GET", "POST"])
def anton_borgstrom():
    return render_template("anton_borgstrom.html")

@app.route("/anton_sendel", methods=["GET", "POST"])
def anton_sendel():
    return render_template("anton_sendel.html")

@app.route("/maria_karnell", methods=["GET", "POST"])
def maria_karnell():
    return render_template("maria_karnell.html")

@app.route("/andrea_holmberg", methods=["GET", "POST"])
def andrea_holmberg():
    return render_template("andrea_holmberg.html")

@app.route("/ludvig_berling", methods=["GET", "POST"])
def ludvig_berling():
    return render_template("ludvig_berling.html")

@app.route("/martin_roginski", methods=["GET", "POST"])
def martin_roginski():
    return render_template("martin_roginski.html")

@app.route("/malin_sagemark", methods=["GET", "POST"])
def malin_sagemark():
    return render_template("malin_sagemark.html")

@app.route("/daniel_forsman", methods=["GET", "POST"])
def daniel_forsman():
    return render_template("daniel_forsman.html")

@app.route("/olivia_broman", methods=["GET", "POST"])
def olivia_broman():
    return render_template("olivia_broman.html")

################################################################################
# interviews END:
################################################################################

@app.route("/placeholder_inspirator", methods=["GET", "POST"])
def placeholder_inspirator():
    return render_template("placeholder_inspirator.html")

if __name__ == '__main__':
    app.run()
