from flask import Flask
from flask import request

app = Flask(__name__)

stored_data = []


@app.route("/")
def hello():
    data_string = "<br>".join(str(data) for data in stored_data)
    return f"Hello, world !<br><br>Stored Data:<br>{data_string}"


@app.route("/webhook", methods=["POST"])
def handleWebhook():
    # get data
    data = request.get_json()

    # store data
    stored_data.append(data)

    # display data in console
    print(data)

    return "OK"


if __name__ == "__main__":
    app.run()
