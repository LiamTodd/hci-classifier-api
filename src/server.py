import dill
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from utils import map_raw_output_to_labels

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

vectorizer = dill.load(open("resources/vectorizer", "rb"))
classifier = dill.load(open("resources/classifier.pkl", "rb"))


@app.route("/classify", methods=["POST"])
@cross_origin()
def classify():

    # Get the JSON data from the request
    request_data = request.get_json()

    # Dummy data to return
    predictions = classifier.predict(vectorizer.transform(request_data.values())).toarray().tolist()
    result = {}
    for i, label in enumerate(request_data.keys()):
        result[label] = {"content": request_data[label], "predictions": map_raw_output_to_labels(predictions[i])}

    # Return the dummy data as JSON
    return jsonify(result)


if __name__ == "__main__":
    app.run()
