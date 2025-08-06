from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fail/<int:score>")
def fail(score):
    return f"You have failed with a score of {score}"


@app.route("/pass/<int:score>")
def pass_score(score):
    return f"You have successfully pass with a score of {score}"


@app.route("/submit", methods=["POST", "GET"])
def submit():
    total_score = 0
    if request.method == "POST":
        DATA440 = float(request.form["data440"])
        ARTI404 = float(request.form["arti404"])
        ARTI406 = float(request.form["arti406"])
        ARTI408 = float(request.form["arti408"])

        total_score = (DATA440 + ARTI404 + ARTI406 + ARTI408) / 4

    if total_score < 50:
        res = redirect(url_for("fail", score=total_score))

    else:
        res = redirect(url_for("pass_score", score=total_score))
    return res


if __name__ == "__main__":
    app.run(debug=True)
