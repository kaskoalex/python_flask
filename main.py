from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return "<h1>Meine Webseite funktioniert</h1><h2>Etwas kleiner</h2>"


@app.route("/home")
def test():
    return "<h1>Schon wieder</h1>"

@app.route("/htmlseite")
def htmlseite():
    return render_template("index.html")   



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
    # "127.0.0.1"-- lokale hosting --
    #app.run(debug=True, host="0.0.0.0")
    # "0.0.0.0" -- erstellung aktive ip adresse auf lokale hosting
