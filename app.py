from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def longest():

    if request.method == "POST":

        text = request.form["text"]
        words = text.split()

        return f"Eng uzun so‘z: {max(words, key=len)}"

    return render_template("index.html")

app.run(debug=True)
