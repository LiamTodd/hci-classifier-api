import dill

APP_USAGE = "app usage"
INCLUSIVENESS = "inclusiveness"
USER_REACTION = "user reaction"
NON_HC = "non human-centric"


def map_raw_output_to_labels(raw_output):
    result = {}
    result[APP_USAGE] = bool(raw_output[0])
    result[INCLUSIVENESS] = bool(raw_output[1])
    result[USER_REACTION] = bool(raw_output[2])
    result[NON_HC] = bool(raw_output[3])
    return result


vectorizer = dill.load(open("resources/vectorizer", "rb"))
classifier = dill.load(open("resources/classifier.pkl", "rb"))


def predict(data):
    predictions = (
        classifier.predict(vectorizer.transform(data.values())).toarray().tolist()
    )
    result = {}
    for i, label in enumerate(data.keys()):
        result[label] = {
            "content": data[label],
            "predictions": map_raw_output_to_labels(predictions[i]),
        }
    return result
