from flask import Flask, render_template, request
from model import predict_result

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    probability = None

    if request.method == "POST":
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        cgpa = float(request.form["cgpa"])
        assignment = float(request.form["assignment"])
        ctt = float(request.form["ctt"])
        internal_300 = float(request.form["internal_300"])
        prev_arrears = int(request.form["prev_arrears"])

        pred, prob = predict_result(
            study_hours,
            attendance,
            cgpa,
            assignment,
            ctt,
            internal_300,
            prev_arrears
        )

        result = "PASS" if pred == 1 else "FAIL"
        probability = prob

    return render_template("index.html", result=result, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
