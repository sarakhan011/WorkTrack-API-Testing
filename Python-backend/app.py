from flask import Flask, jsonify
from models import get_all_employee

app = Flask(__name__)


@app.route("/")
def home():
    return "Employee Management API is running!"


@app.route("/employee")
def employee():

    data = get_all_employee()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)