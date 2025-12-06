from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# For Docker: use host.docker.internal (Windows/macOS)
# On Linux, replace with actual host IP (e.g., 172.17.0.1)
client = MongoClient("mongodb://host.docker.internal:27017/")

db = client["virtual_lab_dashboard"]
labs_collection = db["labs"]

@app.route("/")
def index():
    data = {}
    analytics = {}

    labs = list(labs_collection.find())

    for lab in labs:
        subject = lab["subject"]
        if subject not in data:
            data[subject] = []
            analytics[subject] = []

        not_submitted_students = lab.get("not_submitted", [])
        submitted_students = lab.get("submitted", [])

        # Difficulty score calculation
        capped_not_submitted = min(len(not_submitted_students), 5)
        difficulty_score = round((capped_not_submitted / 5) * 5, 2)
        predicted_marks = round(max(0, 100 - difficulty_score * 20), 2)

        data[subject].append({
            "lab": lab["lab"],
            "submitted": submitted_students,
            "not_submitted": not_submitted_students
        })

        analytics[subject].append({
            "lab": lab["lab"],
            "difficulty": f"{difficulty_score} / 5",
            "predicted_marks": predicted_marks
        })

    return render_template("dashboard.html", data=data, analytics=analytics)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
