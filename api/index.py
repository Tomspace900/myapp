from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

stored_data = []


# Main page
@app.route("/")
def hello():
    return render_template("index.html")


# Webhook endpoint
@app.route("/webhook", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    stored_data.append(data)
    return "OK"


# Data view endpoint
@app.route("/data")
def get_data():
    print(stored_data)
    return render_template("data.html", data=stored_data)


if __name__ == "__main__":
    app.run()
