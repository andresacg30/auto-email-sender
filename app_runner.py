from flask import Flask, render_template
from script.emails import send_email

app = Flask(__name__)

@app.route("/")


def index():
    return render_template("index.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    send_email()
    return render_template("send.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)