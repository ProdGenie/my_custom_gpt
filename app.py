
from flask import Flask, request, jsonify, render_template
import os
import openai

app = Flask(__name__)

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        # Get the word from the request body
        data = request.get_json()
        word = data.get("word")

        if not word:
            return jsonify({"error": "Word is required"}), 400

        # Call OpenAI API (replace with the appropriate prompt for your use case)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide the meaning, synonyms, example sentences, and translations for the word: {word}",
            max_tokens=150
        )

        # Extract the response content
        result = response.choices[0].text.strip()

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
