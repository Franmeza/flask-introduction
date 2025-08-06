from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/pass/<int:score>")
def pass_fail(score):
    return f"<html><body><h1>Congratulations!</h1><p>You have passed the exam with a score of {score}.</p></body></html>"


if __name__ == "__main__":
    app.run(debug=True)
