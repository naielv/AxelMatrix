from flask import Flask, render_template, request, redirect
from utils import add_human, read, configurator
from names import get_full_name
from matrix import make_sim, genhumans
app = Flask(__name__)

file = "data/main.sim"
defaults = "data/defaults.sim"
title = "AxelMatrix Control Panel"
read(file)["iters"]
@app.route('/')
def index():
    iters = read(file)["iters"]
    return render_template('index.html', title=title, current_iter=iters[list(iters)[-1]])

@app.route('/humans', methods=["GET", "POST"])
def humans():
    if request.method == "POST":
        name = request.form["name"]
        if name == "":
            add_human(file, get_full_name())
        else:
            add_human(file, name)
        make_sim(file, 1)
    return render_template('humans.html', humans = read(file)["humans"], title=title)
@app.route("/generate")
def generate():
    make_sim(file, 1)
    return redirect("/")
@app.route("/reset")
def reset():
    configurator(file, [human.dump() for human in genhumans(defaults, 5)])
    make_sim(file, 1)
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8877, debug=True)
 