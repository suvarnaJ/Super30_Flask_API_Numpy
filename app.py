from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)


# =========================================================
# NUMPY ARRAY
# =========================================================

numbers = np.array([
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55
])


# =========================================================
# 1. GET /numbers
# Return the NumPy array
# =========================================================

@app.route("/numbers", methods=["GET"])
def get_numbers():

    return jsonify({
        "numbers": numbers.tolist()
    })


# =========================================================
# 2. GET /mean
# Calculate mean using NumPy
# =========================================================

@app.route("/mean", methods=["GET"])
def get_mean():

    mean_value = np.mean(numbers)

    return jsonify({
        "mean": float(mean_value)
    })


# =========================================================
# 3. GET /median
# Calculate median using NumPy
# =========================================================

@app.route("/median", methods=["GET"])
def get_median():

    median_value = np.median(numbers)

    return jsonify({
        "median": float(median_value)
    })


# =========================================================
# 4. GET /std
# Calculate standard deviation using NumPy
# =========================================================

@app.route("/std", methods=["GET"])
def get_standard_deviation():

    std_value = np.std(numbers)

    return jsonify({
        "standard_deviation": float(std_value)
    })


# =========================================================
# 5. GET /variance
# Calculate variance using NumPy
# =========================================================

@app.route("/variance", methods=["GET"])
def get_variance():

    variance_value = np.var(numbers)

    return jsonify({
        "variance": float(variance_value)
    })


# =========================================================
# 6. GET /maximum
# Find maximum using NumPy
# =========================================================

@app.route("/maximum", methods=["GET"])
def get_maximum():

    maximum_value = np.max(numbers)

    return jsonify({
        "maximum": int(maximum_value)
    })


# =========================================================
# 7. GET /minimum
# Find minimum using NumPy
# =========================================================

@app.route("/minimum", methods=["GET"])
def get_minimum():

    minimum_value = np.min(numbers)

    return jsonify({
        "minimum": int(minimum_value)
    })


# =========================================================
# 8. GET /sum
# Calculate total using NumPy
# =========================================================

@app.route("/sum", methods=["GET"])
def get_sum():

    total = np.sum(numbers)

    return jsonify({
        "sum": int(total)
    })


# =========================================================
# 9. GET /even
# Return even numbers using NumPy filtering
# =========================================================

@app.route("/even", methods=["GET"])
def get_even_numbers():

    even_numbers = numbers[numbers % 2 == 0]

    return jsonify({
        "even": even_numbers.tolist()
    })


# =========================================================
# 10. GET /odd
# Return odd numbers using NumPy filtering
# =========================================================

@app.route("/odd", methods=["GET"])
def get_odd_numbers():

    odd_numbers = numbers[numbers % 2 != 0]

    return jsonify({
        "odd": odd_numbers.tolist()
    })


# =========================================================
# 11. GET /stats
# Return all statistical calculations
# =========================================================

@app.route("/stats", methods=["GET"])
def get_statistics():

    return jsonify({

        "mean": float(np.mean(numbers)),

        "median": float(np.median(numbers)),

        "standard_deviation": float(np.std(numbers)),

        "variance": float(np.var(numbers)),

        "maximum": int(np.max(numbers)),

        "minimum": int(np.min(numbers))

    })


# =========================================================
# 12. GET /table/<number>
# Dynamic multiplication table using NumPy
# =========================================================

@app.route("/table/<int:number>", methods=["GET"])
def multiplication_table(number):

    multipliers = np.arange(1, 11)

    results = number * multipliers

    table = []

    for multiplier, result in zip(multipliers, results):

        table.append({
            "expression": f"{number} x {int(multiplier)}",
            "result": int(result)
        })

    return jsonify({
        "number": number,
        "table": table
    })


# =========================================================
# HOME API
# =========================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Welcome to Flask NumPy Calculation API",
        "endpoints": [
            "/numbers",
            "/mean",
            "/median",
            "/std",
            "/variance",
            "/maximum",
            "/minimum",
            "/sum",
            "/even",
            "/odd",
            "/stats",
            "/table/15"
        ]
    })


# =========================================================
# RUN FLASK APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)