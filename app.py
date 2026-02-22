from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/sobre")
def about():
    return "Começando os estudos sobre APIs com Python."


if __name__ == "__main__":
    app.run(debug=True)