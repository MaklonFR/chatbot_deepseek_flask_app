import re

from flask import Flask, render_template, request
from markupsafe import Markup
import ollama

app = Flask(__name__)

def get_response_from_ollama(user_input):
    # Get the response from the locally running Ollama model
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": user_input}])
    print(response)

    if 'message' in response:
        return response['message']['content']
    else:
        return 'Sorry, something went wrong.'

# Function to process text and replace **bold text** with <strong>bold text</strong>
def process_bold_text(text):
    # Use regular expression to find text wrapped in ** and convert to <strong>
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return re.sub(r'###(.*?)###', r'<strong>\1</strong>', text)    # Match ###bold text###

# Function to handle code blocks wrapped in triple backticks (```)
def process_code_blocks(text):
    # Regex to match code blocks wrapped in triple backticks (```)
    text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response_from_ollama(user_input)
        bot_response = process_bold_text(bot_response)  # Apply bold text processing
        bot_response = process_code_blocks(bot_response)  # Mark as safe HTML
        bot_response = Markup(bot_response)  # Mark as safe HTML

    return render_template("index.html", user_input=user_input, bot_response= bot_response)


if __name__ == "__main__":
    app.run(debug=True)