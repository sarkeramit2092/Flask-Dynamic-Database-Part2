from flask import Flask, render_template, jsonify

app = Flask(__name__)

#JOBS is a list (denoted by [...])

#Each item in the list is a dictionary (denoted by {...})

#So, in short: JOBS is a list of dictionaries.

JOBS = [
  {
    "id": 1,
    "task": "flask framework",
    "time": "2 hours",
    "level": "medium"
  },
    {
    "id": 2,
    "task": "web scraping",
    "time": "3 hours",
    "level": "low"
  },
    {
    "id": 3,
    "task": "GCP",
    "time": "2 hours",
    "level": "high"
  },
  {
    "id": 4,
    "task": "python common",
    "time": "2 hours",
    "level": "high"
  },
  {
    "id": 5,
    "task": "photography",
    "time": "2 hours",
    "level": "low"
  },
]

@app.route ("/")
def home():
  return render_template ("home.html", jobs = JOBS)


@app.route("/api/jobs")  #we have sent the JOBS information as JSON.
#when people say rest API or JSON API or API endpoint -this is what they mean.
def list_jobs():
  return jsonify(JOBS)           #converte JOBS information into a JSON string by a helper function called jsonify.
# jsonify does is it takes any object and converts it into a JSON object.

if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
