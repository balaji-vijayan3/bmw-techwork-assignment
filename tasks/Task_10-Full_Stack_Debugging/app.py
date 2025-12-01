from flask import Flask
import os

app = Flask(__name__)

# Require an environment variable
MESSAGE = os.environ.get("APP_MESSAGE", "default message")  # Will crash if APP_MESSAGE is not set
db_host = os.environ["DB_HOST"]   # Will crash if missing
db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASSWORD"]

@app.route("/")
def home():
    return "This is flask docker app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

