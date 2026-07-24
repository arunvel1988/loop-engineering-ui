from flask import Flask
import logging
import random

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():

    if random.randint(1, 3) == 1:
        app.logger.error("Database timeout")
    else:
        app.logger.info("Request processed successfully")

    return "Hello Agent"

app.run(host="0.0.0.0", port=5000)
