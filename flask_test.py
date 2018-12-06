from flask import Flask, render_template

app = Flask(__name__)


@app.route("/doesu_syogi")
def bottun_FU(x):
    text = x

    return render_template("banmen.html", text=text)


bottun_FU("歩")
app.run(debug=True)
