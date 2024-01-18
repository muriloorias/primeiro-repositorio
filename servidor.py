from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("inicial.html")


@app.route("/anonimo")
def anonimo():
    return render_template("pagina.html")

@app.route("/calculadora")
def calculadora():
    return render_template("calculator.html")


if __name__ == "__main__":
    app.run(debug=True)
