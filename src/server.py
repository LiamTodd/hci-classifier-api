from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from src.utils import predict


app = Flask(__name__)


cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/classify", methods=["POST"])
@cross_origin()
def classify():
    request_data = request.get_json()
    result = predict(request_data)
    return jsonify(result)


@app.route("/bulk-classify", methods=["POST"])
@cross_origin()
def bulk_classify():
    request_data = request.get_json()
    result = []
    for issue in request_data:
        result.append(predict(issue))
    return jsonify(result)


if __name__ == "__main__":
    app.run()
