from flask import Flask
import os

app = Flask(__name__)

# Require an environment variable
MESSAGE = os.environ.get("APP_MESSAGE", "default message")  # Will crash if APP_MESSAGE is not set

@app.route("/")
def home():
    return "This is flask docker app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

