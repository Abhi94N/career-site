from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Atlanta',
    'salary': '$84,000'
  },
  {
    'id': 2,
    'title': 'Lawyer',
    'location': 'New York',
    'salary': '$350,000'
  },
  {
    'id': 3,
    'title': 'DevOps Engineer',
    'location': 'San Francisco',
    'salary': '$240,000'
  },
  {
    'id': 4,
    'title': 'Full Stack Software Engineer',
    'location': 'Remote',
    'salary': '$184,000'
  },
  {
    'id': 5,
    'title': 'Backend Software Engineer',
    'location': 'Remote',
  },
]


@app.route("/")
def index():
  return render_template("home.html", jobs=JOBS, company_name="IllumiDesk")

# api route
@app.route("/api/jobs")
def list_jobs():
  #return information as json
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
