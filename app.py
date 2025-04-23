from flask import Flask, render_template, request
from car_data import car_data
import difflib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        car_name_input = request.form["car_name"].strip().lower()

        # First check exact match (case insensitive)
        matched_car = next((name for name in car_data if car_name_input in name.lower()), None)

        # If not found, use difflib (NLP-style)
        if not matched_car:
            close_matches = difflib.get_close_matches(car_name_input, car_data.keys(), n=1, cutoff=0.4)
            if close_matches:
                matched_car = close_matches[0]

        if matched_car:
            result = {"name": matched_car, "data": car_data[matched_car]}
        else:
            result = {"error": "Car not found."}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()