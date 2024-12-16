from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word = request.form.get("word")
        # Placeholder for processing the word
        return f"You searched for: {word}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
