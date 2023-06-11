from flask import Flask, render_template, request, redirect
from utils import add_human, read, configurator
from matrix import make_sim, genhumans
app = Flask(__name__)

file = "data/main.sim"
defaults = "data/defaults.sim"
title = "AxelMatrix Control Panel"
@app.route('/')
def index():
    return render_template('index.html', iters = read(file)["iters"], title=title)

@app.route('/humans', methods=["GET", "POST"])
def humans():
    if request.method == "POST":
        name = request.form["name"]
        add_human(file, name)
    return render_template('humans.html', humans = read(file)["humans"], title=title)
@app.route("/generate")
def generate():
    make_sim(file, 1)
    return redirect("/")
@app.route("/reset")
def reset():
    configurator(file, [human.dump() for human in genhumans(defaults, 5)])
    return redirect("/humans")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8877, debug=False)
 