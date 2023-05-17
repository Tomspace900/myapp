from flask import Flask, request, jsonify

app = Flask(__name__)

stored_data = []

@app.route("/")
def hello():
    return "Hello, world!"

@app.route("/webhook", methods=["POST"])
def handleWebhook():
    data = request.get_json()
    stored_data.append(data)
    return "OK"

@app.route("/data")
def get_data():
    return jsonify(stored_data)

if __name__ == "__main__":
    app.run()
