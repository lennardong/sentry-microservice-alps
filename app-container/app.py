from flask import Flask, jsonify, request
import vision as v
import requests
from io import BytesIO

app = Flask(__name__)


@app.route("/")
def hello():
    return "Automated License Plate Detection Microservice"


@app.route("/detect", methods=["GET"])
def detect():
    """
    Detect cars and license plates in an image given its URL and return a JSON response
    containing a list of dictionaries with the predominant color of each car and its license plate, if found.

    The image URL should be passed as a "url" query parameter in the request.

    Returns:
        json: A JSON response with a "results" key containing a list of dictionaries.
              Each dictionary has two keys: "color" (a tuple of three floats representing the RGB values)
              and "plate" (the detected license plate as a string). If no cars are detected, an empty list is returned.
        int: The HTTP status code. Returns 400 if the "url" parameter is missing, or the status code from the image request.
    """
    image_url = request.args.get("url")

    if not image_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    response = requests.get(image_url, timeout=10)
    response.raise_for_status()
    image_data = BytesIO(response.content).getvalue()

    results = v.detect(image_data=image_data)
    formatted_results = [{"color": res[0], "plate": res[1]} for res in results]

    return jsonify({"results": formatted_results})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
